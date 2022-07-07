import requests 
from colorama import Fore
from aev import *
print()
try:
    if requests.get('https://google.com'):
        print("İnternet " + r.k1 + "Var")
except:
    print("İnternet " + r.k1 + "Yok")
print()