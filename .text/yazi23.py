from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
                                             d8b           d8,
                                             88P          `8P    d8P
                                            d88               d888888P
 d888b8b   d8888b?88   d8P .d888b,?88,.d88b,888   d8888b   88b  ?88'
d8P' ?88  d8b_,dPd88  d8P' ?8b,   `?88'  ?88?88  d8P' ?88  88P  88P
88b  ,88b 88b    ?8b ,88'    `?8b   88b  d8P 88b 88b  d88 d88   88b
`?88P'`88b`?888P'`?888P'  `?888P'   888888P'  88b`?8888P'd88'   `?8b
                                    88P'
                                   d88
                                   ?8P
""")
