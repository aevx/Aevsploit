from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """

 _______  _______  __   __  _______  _______  ___      _______  ___   _______
|   _   ||       ||  | |  ||       ||       ||   |    |       ||   | |       |
|  |_|  ||    ___||  |_|  ||  _____||    _  ||   |    |   _   ||   | |_     _|
|       ||   |___ |       || |_____ |   |_| ||   |    |  | |  ||   |   |   |
|       ||    ___||       ||_____  ||    ___||   |___ |  |_|  ||   |   |   |
|   _   ||   |___  |     |  _____| ||   |    |       ||       ||   |   |   |
|__| |__||_______|  |___|  |_______||___|    |_______||_______||___|   |___|
""")
