import random,os

os.system("clear")

logolar = ['banner.py','banner1.py','banner2.py','banner3.py','banner4.py','banner5.py','banner6.py','banner7.py','banner8.py','banner9.py','banner10.py']
yazilar = ['yazi.py','yazi1.py','yazi2.py','yazi3.py','yazi4.py','yazi5.py','yazi6.py','yazi7.py','yazi8.py','yazi9.py','yazi10.py','yazi11.py','yazi12.py','yazi13.py','yazi14.py','yazi15.py','yazi16.py','yazi17.py','yazi18.py','yazi19.py','yazi20.py','yazi21.py','yazi22.py','yazi23.py','yazi24.py','yazi25.py','yazi26.py','yazi27.py']

logo = random.choice(logolar)
yazi = random.choice(yazilar)

os.system("python .banner/" + logo)
os.system("python .text/" + yazi)
