import os,zipfile,time
from tqdm import tqdm
from aev import *
try:
 os.system("clear")
 
 os.system("python .logo/logo.py")
 zip_dosyası = input(" [+] Şifreli Zip Dosyasını Girin [+] : ")
 
 try:
  sifre = input(" [+] Wordlist Girin [+] : ")
  
  os.system("clear")
  
  
  zip_dosyası = zipfile.ZipFile(zip_dosyası)
  n_words = len(list(open(sifre, "rb")))
  
  print("Toplam Şifre Sayısı : ",n_words )
  print()
  
  with open(sifre, "rb") as sifre:
      for word in tqdm(sifre, total=n_words):
          try:
            zip_dosyası.extractall(pwd=word.strip())
          except:
              continue
          else:
              print("\n[×] Şifre Bulundu [×] : ", word.decode())
              print()
              exit(0)
  print("[!] Şifre Bulunamadı [!] ")
  menu.input()
 except FileNotFoundError: 
  print("Wordlist Dosyası Bulunmadı")
  menu.input()

except KeyboardInterrupt:
           print()
           print("Zip Brute Sonlandırılıyor...")
           print()
           time.sleep(1)
           exit(0)