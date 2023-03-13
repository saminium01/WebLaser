import os
import sys

def install():
    try:
        import colorama, builtwith, requests
    except:
        os.system('pip install colorama builtwith requests')

install()

from colorama import Fore
from builtwith import builtwith

YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.LIGHTGREEN_EX
WHITE = Fore.WHITE
RESET = Fore.RESET

banner = f'''{CYAN}
 _       __     __    __
| |     / /__  / /_  / /   ____ _________  _____
| | /| / / _ \/ __ \/ /   / __ `/ ___/ _ \/ ___/
| |/ |/ /  __/ /_/ / /___/ /_/ (__  )  __/ /
|__/|__/\___/_.___/_____/\__,_/____/\___/_/
{YELLOW}                        Author: Saminium01
'''
print(banner)

try:
    domain = sys.argv[1]
except:
    print(f"\t\n {WHITE} Usage: python WebLaser.py www.example.com \n")
    sys.exit()

try:
    res = builtwith(f"http://{domain}")
except KeyboardInterrupt:
    print(f"{RED}\n Process Interruted!")

print(f"{GREEN} Results:")
for i in res:
    print(f"{GREEN} {i}", res[i])

print(f"\n {RESET}")
sys.exit()
