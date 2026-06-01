# 🔐 Strong Password Generator (SPG)

A powerful and interactive command-line password generator written in Python.  
This tool allows you to customize your password by choosing which character types to include or exclude — even down to specific characters.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- ✅ Choose password length
- ✅ Exclude entire character types (digits, lowercase, uppercase, special characters)
- ✅ Exclude specific custom characters (e.g., `@ # $` or letters you don't want)
- ✅ Generate multiple passwords without restarting
- ✅ Color-coded terminal output using `colorama`
- ✅ ASCII art banner with credits

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6 or higher installed on your system.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/adelkamell/Strong_Password_Generator---SPG.git
cd Strong_Password_Generator---SPG
Install the required dependency:

bash
pip install colorama
▶️ Running the Program
bash
python password_generator.py
📖 How to Use
Enter password length – type a number (e.g., 12)

Choose character types to exclude – enter numbers 1 to 4 separated by spaces, or press Enter to use all types

Exclude specific characters – type characters separated by spaces (e.g., @ # $), or press Enter to skip

View your generated password

Generate another password – type y or n

Example Walkthrough
text
How many characters do you want your password to have? 16

WARNING : The more options you choose, the lower the security!
Which character types do you NOT want in your password ?
1. digits (0-9)
2. lower case letters (a-z)
3. upper case letters (A-Z)
4. special characters (!@#$%^&* etc.)
Enter the numbers separated by space ('1 3' .e.g), or press Enter to use all types : 1

Enter specific characters you don't want in your password (separate with space) or press Enter to skip : ! @ #

Strong Password : Kv#mP$2xL&yZ*Wq
⚠️ Important Note
The more character types you exclude, the less secure your password becomes.
It is recommended to include at least 3 out of the 4 character types for strong security.

🛠️ Built With
Python 3 – Core language

Colorama – Terminal color support


👨‍💻 Author
Adel Kamel

GitHub: @adelkamell

📄 License
This project is open source and available under the MIT License.

🙌 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

⭐ Show Your Support
If you found this project helpful, please give it a ⭐ on GitHub!