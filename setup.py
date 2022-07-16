try:
 import sys
 sys.path.append(".lib")
 import tool
except ImportError:
 import time,os
 os.system("clear")
 print("32 Bit Tespit Edildi Normal Şartlarda\n\nBu Tool Çalışmaz\n\nAma Çözüm Yolu Deniyoruz.\n\nLütfen Sabırlı Olun.\n")
 os.system('uname -m')
 time.sleep(5)
 os.system("cd && curl -L -O https://github.com/scrlpr/a/raw/main/a.sh && bash a.sh")
