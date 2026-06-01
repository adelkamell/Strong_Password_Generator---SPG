import random
import string
from colorama import Fore, Style

error = f"{Fore.RED}ERROR{Style.RESET_ALL}"
red = Fore.RED
cyan = Fore.CYAN
reset = Style.RESET_ALL


banner = r"""
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

print(banner)

while True :
    characterLength = input(f"{cyan}How many characters do you want your password to have ? {reset}\n")

    if characterLength.isnumeric() :
        characterLength = int(characterLength)
        break 
    else :
        print(error)
        print(f"{red}Please enter a valid number ! \n{reset}")

print(f"\n{red}WARNING : The more options you choose, the lower the security!{reset}")
print(f"{cyan}Which character types do you NOT want in your password ?{reset}")
print("1. digits (0-9)")
print("2. lower case letters (a-z)")
print("3. upper case letters (A-Z)")
print("4. special characters (!@#$%^&* etc.)")
print(f"{cyan}Enter the numbers separated by space ('1 3' .e.g), or press Enter to use all types : {reset}")

while True:
    excludeTypes = input()
    
    if excludeTypes == "":
        excludedTypeSet = set()
        break
    else:
        excludeList = excludeTypes.split()
        excludedTypeSet = set()
        valid = True
        
        for item in excludeList:
            if item in ['1', '2', '3', '4']:
                excludedTypeSet.add(item)
            else:
                print(error)
                print(f"{red}Invalid input! Please enter numbers 1-4 only.{reset}\n")
                print(f"{cyan}Enter the numbers separated by space (e.g., '1 3'), or press Enter to use all types : {reset}")
                valid = False
                break
        
        if valid:
            if len(excludedTypeSet) >= 4:
                print(error)
                print(f"{red}You cannot exclude all character types! Please exclude at most 3 types.{reset}\n")
                print(f"{cyan}Enter the numbers separated by space (e.g., '1 3'), or press Enter to use all types : {reset}")
                continue
            else:
                break

baseChars = ""
if '1' not in excludedTypeSet:
    baseChars += string.digits
if '2' not in excludedTypeSet:
    baseChars += string.ascii_lowercase
if '3' not in excludedTypeSet:
    baseChars += string.ascii_uppercase
if '4' not in excludedTypeSet:
    baseChars += string.punctuation

while True:
    excludedChars = input(f"{cyan}Enter specific characters you don't want in your password (separate with space) or press Enter to skip : {reset}\n")
    
    if excludedChars == "":
        excludedSet = set()
        break
    else:
        excludedList = excludedChars.split()
        excludedSet = set()
        for item in excludedList:
            for char in item:
                excludedSet.add(char)
        
        allChars = baseChars
        remainingChars = [c for c in allChars if c not in excludedSet]
        
        if len(remainingChars) == 0:
            print(error)
            print(f"{red}You have excluded all characters! Cannot generate password.{reset}\n")
            continue
        else:
            break

allowedChars = ""
for char in baseChars:
    if char not in excludedSet:
        allowedChars += char

password = allowedChars

strongPassword = "".join(random.choices(password, k=characterLength))
print(f"{cyan}Strong Password{reset} : {red}{strongPassword}{reset}\n")

while True :
    anotherPassword = input(f"{cyan}Do you want another password (y / n) ? {reset}\n").strip().lower()

    if anotherPassword == "y" :
        strongPassword = "".join(random.choices(password, k=characterLength))
        print(f"{cyan}Another Strong Password{reset} : {red}{strongPassword}{reset}\n")
    elif anotherPassword == "n" :
        break
    else :
        print(error)
        print(f"{red}Invalid input ! Please enter 'y' or 'n' \n{reset}")