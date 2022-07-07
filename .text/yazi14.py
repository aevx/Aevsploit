from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
                               __       __ __
.---.-.-----.--.--.-----.-----|  .-----|__|  |_
|  _  |  -__|  |  |__ --|  _  |  |  _  |  |   _|
|___._|_____|\___/|_____|   __|__|_____|__|____|
                        |__|
""")
