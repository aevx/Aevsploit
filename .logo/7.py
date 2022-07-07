from alive_progress import alive_bar
import time

def animasyon():
    for i in range(100):
        yield
with alive_bar(100) as x:
    for i in animasyon():
        time.sleep(0.03)
        x()