import random, time, sys

class colors():
    r =  "\u001b[31m"
    g =  "\u001b[32m"
    y =  "\u001b[33m"
    b =  "\u001b[34m"
    m = "\u001b[35m"
    c =  "\u001b[36m"
n =  "\u001b[0m"
renkler = [colors.r, colors.g, colors.y, colors.b, colors.m, colors.c]
def loading():
    global bitis
    c = 1
    sayi = 0
    while c < 30:
        aev = c%20
        string ="["+" "*17+"]"
        liste = list(string)
        bir = "❯"
        iki = "❯"
        uc = "❯"
        if aev == 1:
            liste[aev] = random.choice(renkler)+bir+ n
        if aev == 2:
            liste[aev] =random.choice(renkler) + bir+ n
            liste[aev - 1] = random.choice(renkler)+iki + n
        if aev > 2:
            if aev <18:
                liste[aev] =random.choice(renkler) +bir + n
                liste[aev -1] =random.choice(renkler)+iki+ n
                liste[aev-2] =random.choice(renkler)+uc +n
        if aev == 18:
            liste[aev -2] =random.choice(renkler)+ uc+n
            liste[aev - 1] =random.choice(renkler)+iki +n
        if aev == 19:
            liste[aev-2] =random.choice(renkler)+ uc+n


        liste = "".join(liste)
        sys.stdout.write("\r "+liste)
        c += 1
        time.sleep(.1)
if __name__=="__main__":
    loading()