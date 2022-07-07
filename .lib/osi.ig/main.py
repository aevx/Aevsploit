import os, sys,argparse
sys.path.append(os.getcwd()+"/.lib/")
from api import *
from aev import *

try:
  ap = argparse.ArgumentParser()
  ap.add_argument("-u", "--user", required=True)
  args = vars(ap.parse_args())
  
  if args['user']:
   os.system("clear")
   user_info(usrname=args["user"])
   menu.input()

except KeyboardInterrupt:
           print()
           print("İnfogram Sonlandırılıyor...")
           print()
           time.sleep(1)
           exit(0)

except KeyError:
    print('Yanlış Kullanıcı')
    print()
    
except requests.exceptions.ConnectionError:
    print("İnternet Bağlantınızı Kontrol Edin.")
    print()