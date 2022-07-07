from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
 ▄▄▄· ▄▄▄ . ▌ ▐·.▄▄ ·  ▄▄▄·▄▄▌        ▪  ▄▄▄▄▄
▐█ ▀█ ▀▄.▀·▪█·█▌▐█ ▀. ▐█ ▄███•  ▪     ██ •██
▄█▀▀█ ▐▀▀▪▄▐█▐█•▄▀▀▀█▄ ██▀·██▪   ▄█▀▄ ▐█· ▐█.▪
▐█ ▪▐▌▐█▄▄▌ ███ ▐█▄▪▐█▐█▪·•▐█▌▐▌▐█▌.▐▌▐█▌ ▐█▌·
 ▀  ▀  ▀▀▀ . ▀   ▀▀▀▀ .▀   .▀▀▀  ▀█▄▀▪▀▀▀ ▀▀▀""")
