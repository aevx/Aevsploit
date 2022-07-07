import sys,time

def b():
 print()

for i in range(26):
     sys.stdout.write('\r')
     sys.stdout.write("[%-25s] %d%%" % ('#'*i, 4*i))
     sys.stdout.flush()
     sys.stdout.write('\r')
     time.sleep(0.10)
