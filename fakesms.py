import re
import os
import time
import platform
import base64

print("[*] Checking Requirements Module")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
colorama.deinit()
banner = Center.XCenter("""
                _______ _    _  _______     ____  __  __ ______
               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`
              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >
              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |
               \_\                                           /_/
                            \n\n
""")

def check_net1():
    print(termcolor.colored("[*] Checking Internet Connection:- ", 'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(Fore.GREEN+"[*] Connected to the Internet")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(Fore.RED+'[*] No Internet Connection....')


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
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(Fore.GREEN+"\n [+] Thanks For Using Fake-SMS! See You Tomorrow")
            ans = None
        else:
            print(Fore.RED+"\n [+] Not Valid Choice Try again")


def usage1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    print(termcolor.colored('''
      \n    1. Your Country Code Must Be without +
    2. Country Code Example: 91
    3. Your Phone Number Must be Start Without 0
    4. Full Usage: 913443210111

    ..........NOTE: Only One Text Message Is Allowed Per Day...........

      ''', 'magenta'))


def main_check1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
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
        print(termcolor.colored('\n[ X ] Message not sent! Please Try Again SomeTime Or Use Any Eurpose Based Vpn',
                                'red'))
    else:
        print(termcolor.colored(f'\n[ ✔ ] Message sent To:- {x} ', 'green'))


def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check_net1()
        elif platform.system().startswith("Linux"):
            print("\033c")
            check_net1()
        else:
            print(termcolor.colored("Please Use Windows Or Linux OS!", 'red'))
    except KeyboardInterrupt:
        print(termcolor.colored("\n [*]You Pressed The Exit Button!", 'red'))
        quit()
op()
