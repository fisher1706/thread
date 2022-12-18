# https://www.youtube.com/watch?v=hAQb-HbkL8Y&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=4

import time
import threading


def test():
    while True:
        print ("test")
        time.sleep (1)


thr = threading.Timer (5, test)
thr.start ()

for _ in range(3):
    print ("zapel")
    time.sleep (1)

thr.cancel()
print("finish")




