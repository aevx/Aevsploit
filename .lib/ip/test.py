from aev import *
from speedtest import Speedtest
import speedtest as stt

#opın sorç

try:
  menu.bkl()
  st = Speedtest()
  st2 = stt.Speedtest()
  st2.get_best_server()
  i = st.download()
  y = st.upload()
  p = st2.results.ping
  
  i2 = i/1000000
  y2 = y/1000000
  
  x = f"{r.b1}Durum: {r.y1}"
  
  if i2 <= 5:
    d = "Çok Kötü"
  elif i2 <= 10:
    d = "Kötü"
  elif i2 <= 15:
    d = "Normal"
  elif i2 <= 30:
    d = "İdare Eder"
  elif i2 <= 50:
    d = "İyi"
  elif i2 >= 100 or i <= 100:
    d = "MÜKEMMEL"
  else:
    d = "-"
  
  if y2 <= 3:
    d2 = "Kötü"
  elif y2 <= 5:
    d2 = "Normal"
  elif y2 <= 10:
    d2 = "İyi"
  elif y2 <= 20:
    d2 = "Güzel"
  elif y2 <= 50:
    d2 = "Harika"
  elif y2 <= 100 or y >= 100:
    d2 = "Mükemmel"
  else:
    d2 = "-"
    
  if p <= 10:
    d3 = "Mükemmel"
  elif p <= 30:
    d3 = "Güzel"
  elif p <= 50:
    d3 = "İyi"
  elif p <= 110:
    d3 = "Normal"
  elif p <= 150:
    d3 = "Kötü"
  elif p <= 300:
    d3 = "Çok Kötü"
  elif p <= 500 or p >= 500:
    d3 = "Berbat "
  

  
  menu.p3("İndirme Hızı",f"{round(i/1000/1000,1)} Mbit/s {x}{d}")
  menu.p3("Yükleme Hızı",f"{round(y/1000/1000,1)} Mbit/s {x}{d2}")
  print(f"{r.c1}Ping         {r.b1}• {r.p1}{p} Ms {x}{d3}")
  print()
except KeyboardInterrupt:
  pass
except speedtest.ConfigRetrievalError:
  print("\nİnternet Yok\n")