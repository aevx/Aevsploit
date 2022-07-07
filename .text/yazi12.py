from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + '''
eeeee eeee ee   e eeeee eeeee e     eeeee e eeeee
8   8 8    88   8 8   " 8   8 8     8  88 8   8
8eee8 8eee 88  e8 8eeee 8eee8 8e    8   8 8e  8e
88  8 88    8  8     88 88    88    8   8 88  88
88  8 88ee  8ee8  8ee88 88    88eee 8eee8 88  88
''')
