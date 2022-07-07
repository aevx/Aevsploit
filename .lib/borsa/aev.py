import requests,sys
from bs4 import BeautifulSoup
from aev import *

try:
  bot={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
  
  x1 = requests.get("https://m.sabah.com.tr/finans/doviz",headers=bot)
  x2 = requests.get("https://m.sabah.com.tr/finans/altin",headers=bot)
  x3 = requests.get("https://www.binance.com/tr/markets/coinInfo-",headers=bot)
  u = BeautifulSoup(x1.text,'html.parser')
  u2 = BeautifulSoup(x2.text,'html.parser')
  u3 = BeautifulSoup(x3.text,'html.parser')
  
  def kur(x,y):
  	a = u.find_all("span", attrs={"class": "customDovizAltınColorUp"})[x].text
  	menu.p(y,a.strip())
  
  def kuryaz():
  	print()
  	kur(1,"Dolar")
  	kur(4,"Euro")
  	kur(7,"İngiliz Sterlini")
  	kur(-35,"Kanada Doları")
  	kur(-33,"İsviçre Frangı")
  	kur(-27,"100 Japon Yeni")
  	kur(-21,"Norveç Kronu")
  
  def altin(x,y):
          a = u2.find_all("span", attrs={"class": "customDovizAltınColorUp"})[x].text
          menu.p(y,a.strip())
  
  def altinyaz():
  	print()
  	altin(1,"Gram Altın")
  	altin(5,"Çeyrek Altın")
  	altin(-39,"Yarım Altın")
  	altin(-36,"Tam Altın")
  	altin(-33,"Cumhuriyet Altını")
  	altin(-30,"Ata Altın")
  	altin(-26,"Has Altın")
  	altin(-6,"1Kg Altın $")
  	
except:
  pass