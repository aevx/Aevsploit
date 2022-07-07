import os,time
from colorama import Fore
from aev import *

try:

 def b():
  print()
 
 
 def banner():
      menu.bnr("Aev-Tema")
      print(r.c1 + "[01] " + r.k1 + "Temayı Başlat")
      print(r.c1 + "[02] " + r.k1 + "Tema Avantajları [TÜMÜ]")
      print(r.c1 + "[03] " + r.k1 + "Tema Dezavantajları [TÜMÜ]")
      print(r.c1 + "[00] " + r.k1 + "Temadan Çıkar.")
      print(r.c1 + "[x]  " + r.k1 + "Bir Önceki Temayı Geri Getir")
      b()
      
 banner()
 while True:
           aev = input(f"{r.k1}┌──[{r.y}aevsploit{r.b1} • {r.y1}Tema{r.k1}]\n│\n└─⊰ {r.p1}")
 
           if aev == "0" or aev == "00" or aev == "geri":
               print()
               exit(1)

           elif aev == "1" or aev == "01":
            os.system("cp -r $HOME/.termux/* .lib/aev-tema/lib/eski/ > /dev/null 2>&1")
            os.system("cp -r $PREFIX/etc/bash.bashrc .lib/aev-tema/lib/eski/")
            os.system("rm -rf $HOME/.termux/*")
            os.system("rm -rf $PREFIX/etc/bash.bashrc")
            os.system("cp -r .lib/aev-tema/lib/termux.properties $HOME/.termux/")
            print()
            while True:
            	nick = input(r.k1 + "Komut Satırı İçin İsminizi/Nickinizi Yazınız: ")
            	print()
            	if len(nick) == 1:
            		os.system("cp -r .lib/aev-tema/lib/2/bash.bashrc $PREFIX/etc/")
            		break
            	elif len(nick) == 2:
            		os.system("cp -r .lib/aev-tema/lib/3/bash.bashrc $PREFIX/etc/")
            		break
            	elif len(nick) == 3:
            		os.system("cp -r .lib/aev-tema/lib/bash.bashrc $PREFIX/etc/")
            		break
            	elif len(nick) == 4:
            		os.system("cp -r .lib/aev-tema/lib/4/bash.bashrc $PREFIX/etc/")
            		break
            	elif len(nick) == 5:
            		os.system("cp -r .lib/aev-tema/lib/5/bash.bashrc $PREFIX/etc/")
            		break
            	elif len(nick) > 5 or len(nick) < 1:
            		print("En Az 1 En Fazla 5 Haneli Nick Girin")
            		print()
            		continue
            banner = input(r.k1 + "\nBanner İçin İsminizi Girin: ")
            print()
            with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as file:
              data = file.read()
            yenidata = data.replace('nick',nick).replace("banner",banner)

            with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w') as file:
             file.write(yenidata)
             file.close()
            
            while True:
                aev2 = input("\n1 - Mor Mod\n2 - Siyah Mod\n3 - GökYüzü Mavisi\n\nArka Plan Giriniz: ")
                print()
                if aev2 == "01" or aev2 == "1":
                   os.system("cp -r .lib/aev-tema/lib/colors.properties $HOME/.termux/")
                   break
                
                elif aev2 == "02" or aev2 == "2":
                  os.system("cp -r .lib/aev-tema/lib/2/colors.properties $HOME/.termux/")
                  break
                  
                elif aev2 == "03" or aev2 == "3":
                  os.system("cp -r .lib/aev-tema/lib/3/colors.properties $HOME/.termux/")
                  break

                else:
                    print(r.c1 + "\nYanlış Seçenek.\n" + r.k1)

            while True:
                  aev3 = input("\n1 - Yeşil\n2 - Beyaz \n\nYazı Rengi Girin: ")
                  print()
                  if aev3 == "01" or aev3 == "1":
                      with open('/data/data/com.termux/files/home/.termux/colors.properties', 'r') as file:
                          data = file.read()
                          print()
                          print()
                          yenidata = data.replace('FFFFFF',"00FF00")
                          with open('/data/data/com.termux/files/home/.termux/colors.properties', 'w') as file:
                              file.write(yenidata)
                              file.close()
                              break

                  elif aev3 == "02" or aev3 == "2":
                      break
            print(Fore.WHITE + "Tema Tamamlandı. Enter'e Basınız.")
            input()
            break

           elif aev == "2" or aev == "02":
            print(r.k1)
            b()
            print("Size Özel Yeni Komut Satırı.")
            b()
            print("Arka Plan Renginiz Değiştirebileceksiniz.")
            b()
            print("Terminale Sadece aev yazdığınızda Toolu Başlatıcak")
            b()
            print("Ek Tuşlar Gelicek Yukarı Aşşağı Tırnak İşareti Gibi")
            b()
            print("rm -rf komtu yani silme komutu sil olarak da kullanılabilecek sil dosyaismi")
            b()
            print("İstediğiniz İsme Özel Banneriniz Olacak")
            b()
            print("geri yazarak önceki dizine gidersiniz.")
            b()
            print("usr yazarak usr dizine gidersiniz.")
            b()
            print("etc yazarak etc dizine gidersiniz.")
            b()
            print("ls & l komutu artık gizli dosyaları da gösterir.")
            b()
            print("dir komutu artık gizli dosyaları da gösterir.")
            b()
            print("c yazarak clear komutu çalışır.")
            b()
            print("q & e yazarak exit komutu çalışır.")
            b()
            print("gc yazarak git clone komutu çalışır.")
            b()
            print("nano yazarak nano -m (mouse modu) komutu çalışır.")
            b()
            print("p yazarak pwd komutu çalışır.")
            b()
            print("python kodunu py olarak kullanabilirsiniz")
            b()
            continue
            
           elif aev == "3":
            print(r.k1)
            print("Yeni Gelecek Olan Tuşlar Terminali Biraz Küçültebilir")
            b()
            print("Renk İstediğiniz Gibi Olmiyabilir")
            b()
            print("Temayı Sevmeyebilirsiniz")
            b()
            print("Terminal Adında Max 5 Kelimelik Nick Olur.")
            b()
            continue
            
           elif aev == "x" or aev == "xx":
               os.system('clear')
               print('Tema Eski Haline Getiriliyor...')
               time.sleep(1.5)
               os.system('clear')
               
               os.system('rm -rf $HOME/.termux/*')
               os.system("rm -rf $PREFIX/etc/bash.bashrc")

               os.system("mv .lib/aev-tema/lib/eski/*.properties $HOME/.termux/")
               os.system("mv .lib/aev-tema/lib/eski/bash.bashrc $PREFIX/etc/")

               os.system("clear")
               print("Tema Eski Haline Getirildi Lütfen Termuxu Kapatıp Açınız. Aksi tadirde eski temanız görünmez.")
          
           else:
               continue

except KeyboardInterrupt:
           print()
           print("Tema Sonlandırılıyor...")
           print()
           time.sleep(1)
           exit(0) 