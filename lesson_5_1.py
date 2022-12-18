# https://www.youtube.com/watch?v=bmUWWrz1TqY&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=5
from threading import Thread, BoundedSemaphore, currentThread
import time
import random


max_connection = 5
pool = BoundedSemaphore(value=5)


def test():
    with pool:
        slp = random.randint(1, 5)
        print(f"{currentThread().name} - sleep({slp})")
        time.sleep(slp)

for i in range(10):
    Thread(target=test, name=f"thr-{i}").start()
