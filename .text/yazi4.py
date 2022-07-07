from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + '''

                                               888          ,e,   d8
  /~~~8e   e88~~8e  Y88b    /  d88~\ 888-~88e  888  e88~-_   "  _d88__
      88b d888  88b  Y88b  /  C888   888  888b 888 d888   i 888  888
 e88~-888 8888__888   Y88b/    Y88b  888  8888 888 8888   | 888  888
C888  888 Y888    ,    Y8/      888D 888  888P 888 Y888   ' 888  888
 "88_-888  "88___/      Y     \_88P  888-_88"  888  "88_-~  888  "88_/
                                     888
''')
