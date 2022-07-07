from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
____ ____ _  _ ____ ___  _    ____ _ ___
|__| |___ |  | [__  |__] |    |  | |  |
|  | |___  \/  ___] |    |___ |__| |  |
""")
