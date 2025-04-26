import zipfile
import os
import sys

ZIP_PATH = 'secret_docs/secret_docs.zip'
WORDLIST = 'pass.txt'
EXTRACT_TO = 'secret_docs/extracted'

def debug(msg):
    print(f"[DEBUG] {msg}")

def crack_zip(zip_path, wordlist_path):
    # 1. Check file existence
    if not os.path.exists(zip_path):
        debug(f"ZIP file not found: {zip_path}")
        sys.exit(1)
    if not os.path.exists(wordlist_path):
        debug(f"Wordlist not found: {wordlist_path}")
        sys.exit(1)

    debug(f"Opening ZIP: {zip_path}")
    try:
        zf = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile:
        debug("File is not a zip archive or is corrupted.")
        sys.exit(1)

    # 2. Check if it’s encrypted
    try:
        # testzip() returns name of first bad file if any extraction without password fails
        bad = zf.testzip()
        if bad is None:
            debug("ZIP is NOT encrypted (files unpack fine without a password).")
            sys.exit(1)
    except RuntimeError:
        debug("ZIP is encrypted (as expected).")

    # 3. Prepare extract directory
    os.makedirs(EXTRACT_TO, exist_ok=True)

    # 4. Try passwords
    with open(wordlist_path, 'r', errors='ignore') as f:
        for line in f:
            password = line.strip()
            debug(f"Trying password: {password!r}")
            try:
                zf.extractall(path=EXTRACT_TO, pwd=password.encode('utf-8'))
                print(f"[✔] Password found: {password}")
                print(f"Files extracted to: {EXTRACT_TO}")
                return
            except RuntimeError as e:
                # This is what zipfile raises on a bad password
                debug("Bad password")
            except Exception as e:
                debug(f"Unexpected error: {e}")

    print("[✘] Password not found in wordlist.")

if __name__ == "__main__":
    crack_zip(ZIP_PATH, WORDLIST)
