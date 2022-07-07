from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
  ____    ___ __ __  _____ ____  _       ___  ____  ______
 /    |  /  _]  |  |/ ___/|    \| |     /   \|    ||      |
|  o  | /  [_|  |  (   \_ |  o  ) |    |     ||  | |      |
|     ||    _]  |  |\__  ||   _/| |___ |  O  ||  | |_|  |_|
|  _  ||   [_|  :  |/  \ ||  |  |     ||     ||  |   |  |
|  |  ||     |\   / \    ||  |  |     ||     ||  |   |  |
|__|__||_____| \_/   \___||__|  |_____| \___/|____|  |__|
""")
