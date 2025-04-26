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
