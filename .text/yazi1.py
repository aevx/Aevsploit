from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + '''

                            _       _ _
                           | |     (_) |
  __ _  _____   _____ _ __ | | ___  _| |_
 / _` |/ _ \ \ / / __| '_ \| |/ _ \| | __|
| (_| |  __/\ V /\__ \ |_) | | (_) | | |_
 \__,_|\___| \_/ |___/ .__/|_|\___/|_|\__|
                     | |
                     |_|

''')
