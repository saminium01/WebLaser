import os
from sys import platform

try:
    import colorama, builtwith
except:
    os.system('pip install colorama builtwith')
from colorama import Fore
from builtwith import builtwith

BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

def clear():
    if platform == 'win32':
        os.system('cls && title WebLaser')
    elif platform == 'linux' or platform == 'linux2':
        os.system('clear')
    else:
        pass
clear()

banner = f"""{BLUE}
 _       __     __    __
| |     / /__  / /_  / /   ____ _________  _____
| | /| / / _ \/ __ \/ /   / __ `/ ___/ _ \/ ___/
| |/ |/ /  __/ /_/ / /___/ /_/ (__  )  __/ /
|__/|__/\___/_.___/_____/\__,_/____/\___/_/
{YELLOW}                                  Author: Saminium01

"""
print(banner)

target = input(f" {RED}[ + ]{WHITE} Enter your target:: ")

print()

if target.startswith('http://') or target.startswith('https://'):
    res = builtwith(target)
else:
    res = builtwith("http://" + target)


print(BLUE + "Results:")

for i in res:
    print(f"{GREEN} {i}", res[i])

print("\n" + RESET)
