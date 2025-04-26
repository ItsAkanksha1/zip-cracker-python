# Zip Cracker Python

A simple Python script that attempts to crack the password of a password-protected ZIP file using a wordlist. This project demonstrates how to automate the process of testing different passwords for a given ZIP file, making use of Python's `zipfile` module.

## Project Features

- Attempts to crack a password-protected ZIP file using a wordlist.
- Uses the brute-force method by testing each password from a provided text file (`pass.txt`).
- Outputs the successful password if found.
- Supports any ZIP file format with password protection.

## How to Use

1. Clone or download this repository.
2. Place your **password-protected ZIP file** (`secret_docs.zip`) and **wordlist file** (`pass.txt`) in the same folder as the script (`zip_cracker.py`).
3. Ensure you have Python installed on your system (Python 3.6+ recommended).
4. Open the terminal/command prompt and navigate to the project directory.

```bash
cd ~/Desktop/python_projects/zip_crackers

5.Run the Python script:
  python3 zip_cracker.py

The script will start testing each password in the wordlist. If it successfully finds the password, it will print the password and stop.

Requirements
Python 3.6+

zipfile module (comes pre-installed with Python)

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This script is for educational purposes only. Use it responsibly and only on files you own or have permission to test.

Special thanks to all open-source contributors who help improve Python libraries.

yaml
---

### Steps to Add the README:

1. Create a new file named **`README.md`** in the root of your `zip_crackers` folder.
2. Paste the above content into the `README.md`.
3. Save the file.

---

### Optional Steps:

- You can now **commit** the `README.md` file to your GitHub repo:

   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
