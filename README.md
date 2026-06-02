# 🔐 Strong Password Generator

A powerful and interactive command-line password generator written in Python.  
This tool allows you to customize your password by choosing which character types to include or exclude — even down to specific characters.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- ✅ Choose password length
- ✅ Choose how many passwords to generate per batch
- ✅ Exclude entire character types (digits, lowercase, uppercase, special characters)
- ✅ Exclude specific custom characters (e.g., `@ # $` or letters you don't want)
- ✅ Generate multiple passwords without restarting
- ✅ Calculate password entropy (security strength in bits)
- ✅ CLI mode for scripting and automation
- ✅ Copy password to clipboard (optional)
- ✅ Color-coded terminal output using `colorama`
- ✅ ASCII art banner with credits

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6 or higher installed on your system.

### Installation

1. Clone the repository :
```bash
git clone https://github.com/adelkamell/Strong_Password_Generator---SPG.git
cd Strong_Password_Generator---SPG
```

2. Install the required dependencies :
```bash
pip install colorama pyperclip
```

3. ▶️ Running the Program :
```bash
python spg.py
```

## CLI Mode (Non-Interactive)
You can also use the generator directly from command line :

```bash
# Basic usage
python spg.py -l 16

# Generate 5 passwords with no digits
python spg.py -l 20 --no-digits -n 5

# Exclude specific characters and copy to clipboard
python spg.py -l 24 --no-special -e "! @ # $ %" --clip

# Hide banner
python spg.py -l 16 --no-banner

# See all options
python spg.py -h
```
## 📖 How to Use
Interactive Mode (run without arguments):
Enter password length – type a number (e.g., 12)

Enter how many passwords per batch – press Enter for 1, or type a number

Choose character types to exclude – enter numbers 1 to 4 separated by spaces, or press Enter to use all types

Exclude specific characters – type characters separated by spaces (e.g., @ # $), or press Enter to skip

View your generated password(s) with entropy score

Generate another password – type y or n

## Command Line Options:
Option	Description
-l, --length	Password length (default: 16)
--no-digits	Exclude digits
--no-lower	Exclude lowercase letters
--no-upper	Exclude uppercase letters
--no-special	Exclude special characters
-e, --exclude	Specific characters to exclude
-n, --count	Number of passwords to generate (default: 1)
--no-banner	Hide the banner
--clip	Copy first password to clipboard

## Example Walkthrough
text
How many characters? 16

How many passwords per batch? (press Enter for 1) 2

WARNING : The more options you choose, the lower the security!
Which character types do you NOT want in your password ?
1. digits (0-9)
2. lower case letters (a-z)
3. upper case letters (A-Z)
4. special characters (!@#$%^&* etc.)
Enter numbers separated by space, or press Enter for all types : 1

Enter specific characters to exclude (separate with space), or press Enter to skip: ! @ #

==================================================
Password 1: Kv#mP$2xL&yZ*Wq
Entropy: 95.3 bits  Very Strong
------------------------------
Password 2: R*tYzQ$3mNpL&xV
Entropy: 95.3 bits  Very Strong
==================================================

## ⚠️ Important Note
- The more character types you exclude, the less secure your password becomes.

- It is recommended to include at least 3 out of the 4 character types for strong security.

- Passwords are generated using Python's secrets module (cryptographically secure).

## 🛠️ Built With
- Python 3 – Core language

- Colorama – Terminal color support

- pyperclip – Clipboard support (optional)

## 👨‍💻 Author
- Adel Kamel

## GitHub: @adelkamell

## 📄 License
- This project is open source and available under the MIT License.

## 🙌 Contributing
- Contributions, issues, and feature requests are welcome!

- Feel free to check the issues page.

## ⭐ Show Your Support
- If you found this project helpful, please give it a ⭐ on GitHub!