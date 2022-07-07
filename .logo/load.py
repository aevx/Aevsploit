import os,random

liste = ['1.py','2.py','3.py','4.py','5.py','6.py','7.py','8.py','9.py','10.py','11.py']

a = random.choice(liste)

os.system("python .logo/" + a)