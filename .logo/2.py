import sys,time

for x in range(0,11):
  sys.stdout.write("\u001b[1000D")
  sys.stdout.write("*************** ")
  sys.stdout.write(str(x))
  sys.stdout.write(" *************** ")
  sys.stdout.flush()
  time.sleep(.3)
