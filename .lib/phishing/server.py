import os,sys,time
from colorama import Fore

def c():
  os.system("clear")
  
def tb(x):
  os.system(x)

class r():
  b = Fore.WHITE
  k = Fore.RED
  y = Fore.GREEN
  m = Fore.BLUE
  cy = Fore.CYAN
  byz = Fore.WHITE
  pmb = Fore.MAGENTA
  sr = Fore.YELLOW

c()

try:
  tb("python .logo/logo.py")
  print(r.b + "Örnek:" + r.k + "             /sdcard/instatelif/")
  print(r.b + "Sdcard Dizini:" + r.k + "     /sdcard/")
  print(r.b + "Termux Dizini:" + r.k + "     /data/data/com.termux/files/home/\n")
  print(r.b + "Durdurmak İçin " + r.k + "Ctrl + C" + r.b + " Yapınız.\n")
  
  sc = input(r.k + "Script Dizini Giriniz: " + r.b)
  port = input(r.k + "Port Girin: " + r.b)
  
  c()
  
  print(r.b + "Local Hostunuz: " + r.k + "127.0.0.1:" + port)
  print("\n"*5 + Fore.GREEN)
  os.system("\nxdg-open http://127.0.0.1:" + port)
  
  os.system(f"cd {sc} && php -S 127.0.0.1:{port}")

except KeyboardInterrupt:
  print()
  print("Server Sonlandırılıyor...")
  print()
  time.sleep(1)
  exit(0)