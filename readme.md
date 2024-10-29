Here's a README file draft for your ACS-1100 project, based on the details provided. I've outlined the purpose, installation, usage, and an overview of the files included in the project.

---

# ACS-1100 Project

This project provides a simple Python-based user login system that allows users to access account information securely based on stored usernames and passwords. Once logged in, users can view account details, including their balance.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Future Enhancements](#future-enhancements)

## Installation

1. **Clone the Repository**: Clone the project files from GitHub.
   ```bash
   git clone https://github.com/your-username/ACS-1100-Project.git
   cd ACS-1100-Project
   ```

2. **Dependencies**: Ensure you have Python 3 installed. This project has no external dependencies.

## Usage

To use this program:

1. Ensure that `data.txt` is located in the same directory as `index4.py`.
2. Run the Python script:
   ```bash
   python3 index4.py
   ```
3. Enter a username and password when prompted:
   - **Example User Accounts**:
     - Username: `aman`, Password: `1234` (Andy Allman)
     - Username: `betho`, Password: `pa$$word` (Beth Beto)
     - Username: `camcam`, Password: `default` (Cameron Clay)
4. Upon successful login, the program will display the user's name and account balance. If the credentials are incorrect, the program will prompt for re-entry.

## File Overview

- **index4.py**: Main program file containing the login system logic. It reads user credentials from `data.txt`, compares inputs, and displays account information.
- **data.txt**: Data file storing user account information in the format `username,password,full name,balance`.

## STRETCH CHALLENGES

Possible improvements could include:
- Encrypting passwords for enhanced security.
- Adding functionality to create or delete accounts.
- Expanding the login validation to include email or phone-based authentication.
- Storing user data in a database rather than a text file.
