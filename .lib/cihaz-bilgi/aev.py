import os,time
import platform as p
from colorama import Fore

def b():
 print()

w = Fore.WHITE
m = Fore.MAGENTA


bits, linkage = p.architecture()

build_num, build_date = p.python_build()

b()
print(w + "Bit   : " + m + bits)
print(w + "Makine : " + m + p.machine())
print(w + "Host : " + m + p.node())
print(w + "Platform : " + m + p.platform())
print(w + "İşlemci : " + m + p.processor())
print(w + "Sistem Adı : " + m + p.system())
print(w + "Sistem Versyonu : " + m + p.version())
b()