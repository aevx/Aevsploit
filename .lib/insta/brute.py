import os,time
from colorama import Fore
from aev import *

try:
 menu.bnr("IG - Brute")
 print()
 print("Tool Sahibi/Via : github.com/keralahacker\n")
 a = input("Kullanıcı Adı Girin: ")
 so.c()
 b = input("Şifre Dosyası Girin: ")
 so.c()
 so.s(f"python .lib/insta/Ig-brute/instagram.py {a} {b}")

except KeyboardInterrupt:
  menu.son("Instagram Brute")