from colorama import Fore, Style
import random

aev = Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN,Fore.WHITE

renk = random.choice(aev)

print (renk + """
.sSSSSs.    .sSSSSs.    .sSSS s.    .sSSSSSSSs. .sSSSSs.    SSSSS
S SSSSSSSs. S SSSSSSSs. S SSS SSSs. S SSS SSSS' S SSSSSSSs. S SSS
S  SS SSSSS S  SS SSSS' S  SS SSSSS S  SS       S  SS SSSSS S  SS
S..SSsSSSSS S..SS       S..SS SSSSS `SSSSsSSSa. S..SS SSSSS S..SS
S:::S SSSSS S:::SSSS     S::S SSSS  .sSSS SSSSS S:::SsSSSSS S:::S
S;;;S SSSSS S;;;S         S;S SSS   S;;;S SSSSS S;;;S       S;;;S
S%%%S SSSSS S%%%S SSSSS    SS SS    S%%%S SSSSS S%%%S       S%%%S SSSSS
SSSSS SSSSS SSSSSsSS;:'     SsS     SSSSSsSSSSS SSSSS       SSSSSsSS;:'


.sSSSSs.    SSSSS .sSSSSSSSSSSSSSs.
S SSSSSSSs. S SSS SSSSS S SSS SSSSS
S  SS SSSSS S  SS SSSSS S  SS SSSSS
S..SS SSSSS S..SS `:S:' S..SS `:S:'
S:::S SSSSS S:::S       S:::S
S;;;S SSSSS S;;;S       S;;;S
S%%%S SSSSS S%%%S       S%%%S
SSSSSsSSSSS SSSSS       SSSSS
""")
