import itertools
import threading
import time
import sys

x = False
def animasyon():
  for c in itertools.cycle(['|', '/', '-', '\\']):
        if x:
            break
        sys.stdout.write('\rYükleniyor ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animasyon)
t.start()

time.sleep(3)
x = True
