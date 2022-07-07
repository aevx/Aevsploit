from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + '''
   __    ____  _  _  ___  ____  __    _____  ____  ____
  /__\  ( ___)( \/ )/ __)(  _ \(  )  (  _  )(_  _)(_  _)
 /(__)\  )__)  \  / \__ \ )___/ )(__  )(_)(  _)(_   )(
(__)(__)(____)  \/  (___/(__)  (____)(_____)(____) (__)
''')
