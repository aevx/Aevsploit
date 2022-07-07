import random
print()

try:
 
 veri = int(input("Hane Sayısını Girin: "))
 
 def parola(uzunluk):
     harfler = '.abcdefgjklmnoprstyvyzxwq'
     sayi = '0123456789'
     mod = str(harfler + sayi)
 
     sonuc = ''.join(random.choice(mod) for i in range(uzunluk))
     return sonuc
 print()
 print(parola(veri))
 print()
 
except ValueError:
 print()
 print("Yanlış Seçenek.")
 print()
 
except KeyboardInterrupt:
 print()
 print("Çıkış Yapılıyor...")
 print()
 exit()