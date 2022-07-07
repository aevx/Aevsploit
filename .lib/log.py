import os, time, sys, random
from aev import *

try:

 os.system("clear")
 print('\n\n\n\n\n')
 
 os.system("python .logo/logo.py")
 
 print(r.c1 + "[01] " + r.k1 + "Log Dizinini Gösterir.")
 print(r.c1 + "[02] " + r.k1 + "Log Dosyasını Gösterir.")
 print(r.c1 + "[03] " + r.k1 + "Log Dosyasını Siler.")
 print(r.c1 + "[00] " + r.k1 + "Çık.")
 
 print()
 while True:
           aev = input(r.b1 + "aevsploit (" + r.k1 + "LOG" + r.b1 + ")" + r.m1 + " 》 ")
           dosya = open("log.txt","a+")
           dosya.write(aev+'\n')
           dosya.close()
 
           if aev=="01" or aev == "1":
              print(r.k1 + "Log Dizini:" + r.m1 + "/data/data/com.termux/files/home/Aevsploit-Assistant/log.txt")
 
           elif aev=="02" or aev == "2":
                os.system("more log.txt")
 
           elif aev =="03" or aev == "3":
                os.system("rm -rf log.txt")
                print(r.k1 + "Log Dosyası Silindi...")
                time.sleep(1)
                
           elif aev == "00" or aev == "0":
             exit()
 
           elif aev=="clear":
                 os.system("clear")
 
           elif aev=="geri":
                exit()
 
           elif aev=="exit":
                print()
                print(r.k1 + "Çıkmak İçin CTRL TUŞU + Z BASINIZ.")
                print()

except KeyboardInterrupt:
           print()
           print("Log Sonlandırılıyor...")
           print()
           time.sleep(1)
           exit(0)