import time
import sys

x = 0

while x == 0:
        aev = 'aevsploit başlatılıyor...'
        for x in range(len(aev)):
                sys.stdout.write('\r'+'[*] '+aev[:x]+aev[x:].capitalize())
                sys.stdout.flush()
                time.sleep(0.1)
                x + x+ 1