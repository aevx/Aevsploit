import os,random
from aev import *

try:
    dx = "cd site/"
    
    so.c()
    print(r.k + "Port Giriniz Örnek: 8080\n")
    port = input(r.c1 + "Port > ")
    so.c()
    if port.strip() == "" or port.strip() == " " or port.strip() == "    ":
      port = random.randint(1000,9999)
      so.c()
    
    def kur():
      time.sleep(1)
      os.system(f"{dx} && php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
        
    print(f"\n\n\n{r.b1}Site: {r.s}localhost:{port}\n\n\n")
    print(f"{r.b}Durdurmak İçin {r.k} CTRL + C {r.b} Tuşlarına Basınız.")
    os.system(f"{dx} && killall -2 php > /dev/null 2>&1")
    os.system(f"{dx} && fuser -k {port}/tcp > /dev/null 2>&1")
    kur()

except KeyboardInterrupt:
    exit()