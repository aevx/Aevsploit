from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
 _______ _______ _    _ _______  _____          _____  _____ _______
 |_____| |______  \  /  |______ |_____] |      |     |   |      |
 |     | |______   \/   ______| |       |_____ |_____| __|__    |
""")
