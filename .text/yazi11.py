from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + '''
                                        888        d8b 888
                                        888        Y8P 888
                                        888            888
 8888b.  .d88b. 888  888.d8888b 88888b. 888 .d88b. 888 888888
    "88bd8P  Y8b888  88888K     888 "88b888d88""88b888 888
.d88888888888888Y88  88P"Y8888b.888  888888888  888888 888
888  888Y8b.     Y8bd8P      X88888 d88P888Y88..88P888 Y88b.
"Y888888 "Y8888   Y88P   88888P'88888P" 888 "Y88P" 888 "Y888
                                888
                                888
                                888
''')
