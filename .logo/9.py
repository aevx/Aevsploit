from time import sleep

zaman = 0.030

def aev(s):
    for i in range(101):
        sharp = "#"*(i//10)
        i = str(i)
        s = "|{:>10}".format(sharp) + i.rjust(1) + "{:<10}|".format(sharp)
        print("\r" + s, end = "")
        sleep(zaman)
    print()

aev(zaman)
