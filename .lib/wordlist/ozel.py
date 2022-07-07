import os,random,time
from colorama import Fore
from aev import *

def p():
 print()
 
try:
 menu.bnr("Aev.Wordlist")
 hane=input(r.k1 + "Wordlistiniz En Fazla Kaç Haneli Olsun?: " + r.b1)
 p()
 dizin=input(r.k1 + "Dosya İsmi Giriniz: " + r.b1)
 p()
 yazi = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZxwqXWQ0123456789.@_+!*?"
 p()
 print("wordlist -m 1 -M "+ hane + " -o " + dizin + " " + yazi)
 p()
 print(Fore.YELLOW + "Oluşturuluyor...")
 p()
 so.s("cd /sdcard")
 os.system("wordlist -m 1 -M "+ hane + " -o " + dizin + " " + yazi)
 p()
 menu.sd(dizin)
 menu.input()
except KeyboardInterrupt:
           print()
           print("Wordlist Sonlandırılıyor...")
           print()
           time.sleep(1)
           exit(0)