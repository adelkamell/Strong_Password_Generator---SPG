#!/usr/bin/env python3
"""
Strong Password Generator (SPG)
A command-line tool to generate custom passwords with exclusion options.
Author: Adel Kamel | GitHub: @adelkamell
Repo: https://github.com/adelkamell/Strong_Password_Generator---SPG.git
"""

import string
import secrets
import sys
import argparse
import math

try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False

from colorama import Fore, Style, init
init(autoreset=True)

# --- Color definitions ---
error = f"{Fore.RED}ERROR{Style.RESET_ALL}"
red = Fore.RED
cyan = Fore.CYAN
reset = Style.RESET_ALL

# --- Banner ---
BANNER = r"""
  ______   _________  _______      ___   ____  _____   ______                       
.' ____ \ |  _   _  ||_   __ \   .'   `.|_   \|_   _|.' ___  |                      
| (___ \_||_/ | | \_|  | |__) | /  .-.  \ |   \ | | / .'   \_|                      
 _.____`.     | |      |  __ /  | |   | | | |\ \| | | |   ____                      
| \____) |   _| |_    _| |  \ \_\  `-'  /_| |_\   |_\ `.___]  |                     
 \______.'  |_____|  |____| |___|`.___.'|_____|\____|`._____.'                      
                                                          
 _______     _       ______    ______  ____      ____   ___   _______     ______    
|_   __ \   / \    .' ____ \ .' ____ \|_  _|    |_  _|.'   `.|_   __ \   |_   _ `.  
  | |__) | / _ \   | (___ \_|| (___ \_| \ \  /\  / / /  .-.  \ | |__) |    | | `. \ 
  |  ___/ / ___ \   _.____`.  _.____`.   \ \/  \/ /  | |   | | |  __ /     | |  | | 
 _| |_  _/ /   \ \_| \____) || \____) |   \  /\  /   \  `-'  /_| |  \ \_  _| |_.' / 
|_____||____| |____|\______.' \______.'    \/  \/     `.___.'|____| |___||______.'  
                                                                                    
        CREATED BY AdelKamel :   https://github.com/adelkamell
"""

def build_charset(excluded_categories: set, excluded_chars: set) -> str:
    """Build character set from allowed categories minus specific excluded characters."""
    base = ""
    if '1' not in excluded_categories:
        base += string.digits
    if '2' not in excluded_categories:
        base += string.ascii_lowercase
    if '3' not in excluded_categories:
        base += string.ascii_uppercase
    if '4' not in excluded_categories:
        base += string.punctuation

    return ''.join(c for c in base if c not in excluded_chars)

def generate_passwords(length: int, charset: str, count: int = 1) -> list:
    """Generate a list of cryptographically strong passwords."""
    if len(charset) == 0:
        raise ValueError("Character set is empty")
    return [''.join(secrets.choice(charset) for _ in range(length)) for _ in range(count)]

def entropy_bits(length: int, charset_size: int) -> float:
    """Calculate password entropy in bits."""
    if charset_size < 2:
        return 0.0
    return length * math.log2(charset_size)

def strength_label(entropy: float) -> str:
    """Return a colored strength label based on entropy."""
    if entropy >= 80:
        return f"{Fore.GREEN}Very Strong{reset}"
    elif entropy >= 60:
        return f"{Fore.YELLOW}Strong{reset}"
    elif entropy >= 40:
        return f"{Fore.YELLOW}Moderate{reset}"
    else:
        return f"{Fore.RED}Weak{reset}"

def cli_mode(args):
    """Non‑interactive mode using command‑line arguments."""
    if not args.no_banner:
        print(BANNER)

    # Build excluded categories set from flags
    excluded_cats = set()
    if args.no_digits:
        excluded_cats.add('1')
    if args.no_lower:
        excluded_cats.add('2')
    if args.no_upper:
        excluded_cats.add('3')
    if args.no_special:
        excluded_cats.add('4')

    if len(excluded_cats) == 4:
        print(error, f"{red}Cannot exclude all character types!{reset}")
        sys.exit(1)

    # Excluded specific characters
    excluded_chars = set(args.exclude) if args.exclude else set()

    charset = build_charset(excluded_cats, excluded_chars)
    if not charset:
        print(error, f"{red}No characters available to generate password.{reset}")
        sys.exit(1)

    passwords = generate_passwords(args.length, charset, args.count)

    for i, pwd in enumerate(passwords, 1):
        ent = entropy_bits(len(pwd), len(charset))
        print(f"{cyan}Password {i}{reset}: {red}{pwd}{reset}   {cyan}Entropy{reset}: {ent:.1f} bits ({strength_label(ent)})")

    if args.clip:
        if HAS_PYPERCLIP:
            pyperclip.copy(passwords[0])
            print(f"{cyan}First password copied to clipboard.{reset}")
        else:
            print(f"{red}pyperclip not installed. Install it to use --clip.{reset}")

def interactive_mode():
    """Original interactive flow with batch generation and 'another password' prompt."""
    print(BANNER)

    # Password length
    while True:
        length_input = input(f"{cyan}How many characters? {reset}\n")
        if length_input.isnumeric():
            length = int(length_input)
            break
        print(error)
        print(f"{red}Please enter a valid number!{reset}\n")

    # Number of passwords to generate per batch
    while True:
        count_input = input(f"{cyan}How many passwords per batch? (press Enter for 1) {reset}\n")
        if count_input == "":
            count = 1
            break
        if count_input.isnumeric() and int(count_input) > 0:
            count = int(count_input)
            break
        print(error)
        print(f"{red}Enter a positive number or press Enter.{reset}\n")

    # Category exclusions
    print(f"\n{red}WARNING: Excluding types lowers security!{reset}")
    print(f"{cyan}Which types do you NOT want?{reset}")
    print("1. digits (0-9)")
    print("2. lowercase (a-z)")
    print("3. uppercase (A-Z)")
    print("4. special (!@#$%^&* etc.)")
    print(f"{cyan}Enter numbers separated by space, or press Enter for all types: {reset}")

    while True:
        exclude_input = input().strip()
        if exclude_input == "":
            excluded_cats = set()
            break
        items = exclude_input.split()
        valid = True
        temp_set = set()
        for item in items:
            if item in ['1', '2', '3', '4']:
                temp_set.add(item)
            else:
                print(error)
                print(f"{red}Invalid input! Use numbers 1-4 only.{reset}\n")
                valid = False
                break
        if not valid:
            continue
        if len(temp_set) >= 4:
            print(error)
            print(f"{red}You cannot exclude all types. At most 3.{reset}\n")
            continue
        excluded_cats = temp_set
        break

    # Specific character exclusions
    print(f"{cyan}Enter specific characters to exclude (separate with space), or press Enter to skip: {reset}")
    excluded_chars = set()
    while True:
        user_excl = input().strip()
        if user_excl == "":
            break
        items = user_excl.split()
        for item in items:
            for c in item:
                excluded_chars.add(c)
        # Check if any characters remain
        temp_charset = build_charset(excluded_cats, excluded_chars)
        if not temp_charset:
            print(error)
            print(f"{red}No characters left! Try again.{reset}\n")
            excluded_chars.clear()
            continue
        break

    charset = build_charset(excluded_cats, excluded_chars)

    # Main generation loop – user can request more passwords with same settings
    while True:
        passwords = generate_passwords(length, charset, count)
        print("\n" + "=" * 50)
        for i, pwd in enumerate(passwords, 1):
            ent = entropy_bits(len(pwd), len(charset))
            print(f"{cyan}Password {i}{reset}: {red}{pwd}{reset}")
            print(f"{cyan}Entropy{reset}: {ent:.1f} bits  {strength_label(ent)}")
            if i < len(passwords):
                print("-" * 30)
        print("=" * 50 + "\n")

        # Ask if user wants another batch
        while True:
            another = input(f"{cyan}Do you want another password? (y/n) {reset}\n").strip().lower()
            if another == 'y':
                break  # break inner loop, generate again
            elif another == 'n':
                return   # exit interactive mode entirely
            else:
                print(error)
                print(f"{red}Invalid input! Please enter 'y' or 'n'.{reset}\n")

def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description="Strong Password Generator",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="Run without arguments for interactive mode."
        )
        parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
        parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
        parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
        parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
        parser.add_argument("--no-special", action="store_true", help="Exclude special characters")
        parser.add_argument("-e", "--exclude", nargs="*", default=[], help="Specific characters to exclude")
        parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
        parser.add_argument("--no-banner", action="store_true", help="Hide the banner")
        parser.add_argument("--clip", action="store_true", help="Copy first password to clipboard (requires pyperclip)")
        args = parser.parse_args()
        cli_mode(args)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()