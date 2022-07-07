#AEVSPLOİT OPEN SOURCE
import os,time

try:
  from bs4 import BeautifulSoup
  import requests
except ModuleNotFoundError:
    os.system("apt install openssl -y > /dev/null 2<&1")
    os.system("pip install requests > /dev/null 2<&1")
    os.system("pip install colorama  > /dev/null 2<&1")
    os.system('pip install bs4 > /dev/null 2<&1')
    
from bs4 import BeautifulSoup
import requests,time,os

class r():
	def pr(x,y,z,q):
		print(f"\033[{x};3{y};4{z}m{q}" )
	sa = "\033[5;30;40m"
	g = "\033[1;30m"
	k = "\033[0;31m"
	k1 = "\033[1;31m"
	y = "\033[0;32m"
	y1 = "\033[1;32m"
	s = "\033[0;33m"
	s1 = "\033[1;33m"
	m = "\033[0;34m"
	m1 = "\033[1;34m"
	p = "\033[0;35m"
	p1 = "\033[1;35m"
	c = "\033[0;36m"
	c1 = "\033[1;36m"
	b = "\033[0;37m"
	b1 = "\033[1;37m"
	rst = '\033[0m'

class menu():
  def input():
    input(f"\n{r.b1}Ana Menüye Dönmek İçin {r.k1}Enter'a {r.b1}Tıklayınız.")
  def ctrlc():
    print(f"{r.b1}Çıkmak İçin {r.k1}Ctrl + C {r.b1}Tuşlarına Basınız.\n")
  def p(x,y):
    print(f"{r.p1}{x}{r.b1} - {r.c1}{y}")
  def p2(x,y="+"):
   print(f"{r.b1}[{r.k1}{y}{r.b1}]{r.p1} " + x)
  def p3(x,y):
    print(f"{r.c1}{x}{r.b1} • {r.p1}{y}")
  def bnr(x):
    print(r.c1)
    os.system(f'clear && figlet -f Doom {x}')
  def els():
    print(p1 + "Yanlış Seçenek")
  def son(x):
    print(f"{r.k1}{x} {r.b1}Sonlandırılıyor...")
    time.sleep(1)
  def sd(x = ""):
    print(f"{r.b1}Dosya{r.k1} /sdcard/{x} {r.b1}Dizinine Kaydedildi.")
  def bkl():
    print(r.s + "\nLütfen Bekleyiniz...\n")
    
class so(): #os tersi
  def s(x):#sistem
    os.system(x)
  def c():#clear
    os.system("clear")
  def dt(a,b):#dosya taşıma
    os.system(f"cp -r {a} {b}")
  def sl(*x):#sil
    for l in x:
      os.system(f"rm -rf {l}")

class hash():
  def enc():
      a = input(r.k1 + "aev hash İle Hashlenicek Metini Gir: " + r.b1).lower()
      print()
      print()
      b = a[::-1]
      c = b.replace("a","Z9").replace("b","Y8").replace("c","V7").replace("ç","U6").replace("d","T5").replace("e","S4").replace("f","R3").replace("g","P2").replace("ğ","O1").replace("h","N2").replace("ı","M3").replace("i","L4").replace("j","K5").replace("k","J6").replace("l","I7").replace("m","H6").replace("n","G9").replace("o","F8").replace("ö","E7").replace("p","D6").replace("r","C5").replace("s","B4").replace("ş","A3").replace("t","1A").replace("u","2B").replace("ü","3C").replace("v","4D").replace("y","5E").replace("z","6F").replace("x","7G").replace("w","8H").replace("q","9I").replace(".","1J").replace(",","2K").replace(" ","^")
      d = c[::-1]
      e = d.replace("1","z+").replace("2","x-").replace("3","*!").replace("4","?!").replace("5","@#").replace("6","_-").replace("7","(").replace("8","^=").replace("9","%^").replace("0","=-")
      f = e[::-1]
      g = f.replace("+","0").replace("-","1").replace("!","2").replace("?","3").replace("@","4").replace("_","5").replace("(","6").replace("^","7").replace("%","8").replace("Д","9")
      h = g[::-1]
      print(r.k1 + "Aev Hash İle Şifrelenmiş Şifreniz: \n")
      print(r.y + h + r.k1)
  
  def dec():
      a = input(r.k1 + "\nAEV hash Encode Metini Gir: ")
      print()
      print()
      b = a[::-1]
      c = b.replace("0","+").replace("1","-").replace("2","!").replace("3","?").replace("4","@").replace("5","_").replace("6","(").replace("7","^").replace("8","%").replace("9","Д")
      d = c[::-1]
      e = d.replace("z+","1").replace("x-","2").replace("*!","3").replace("?!","4").replace("@#","5").replace("_-","6").replace("(","7").replace("^=","8").replace("%^","9").replace("=-","0")
      f = e[::-1]
      g = f.replace("Z9","a").replace("Y8","b").replace("V7","c").replace("U6","ç").replace("T5","d").replace("S4","e").replace("R3","f").replace("P2","g").replace("O1","ğ").replace("N2","h").replace("M3","ı").replace("L4","i").replace("K5","j").replace("J6","k").replace("I7","l").replace("H6","m").replace("G9","n").replace("F8","o").replace("E7","ö").replace("D6","p").replace("C5","r").replace("B4","s").replace("A3","ş").replace("1A","t").replace("2B","u").replace("3C","ü").replace("4D","v").replace("5E","y").replace("6F","z").replace("7G","x").replace("8H","w").replace("9I","q").replace("J1",".").replace(",","2K").replace("^", " ")
      h = g[::-1]
      print(r.k1 + "Decode: " + r.y1 + h + r.k1 + "\n")

#######################################