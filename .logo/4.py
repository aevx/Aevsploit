import time,sys

print("Yükleniyor", end ="")
aev = 3
aev_hiz = 4                                                     
aev_str = "." * 6
while aev < 5:
    for i, char in enumerate(aev_str):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1.0 / aev_hiz)
    i += 1
    sys.stdout.write("\b" * i + " " * i + "\b" * i)
    sys.stdout.flush()
    aev += 1