# https://www.youtube.com/watch?v=bmUWWrz1TqY&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=5
import threading
from threading import currentThread
import time
import random


def test(barrier):
    slp = random.randint(3, 7)
    time.sleep (slp)
    print(f"Thread [{currentThread().name}] start at ({time.ctime()})")

    barrier.wait()
    print(f"Thread [{currentThread().name}] arrive barrier at ({time.ctime()})")


bar = threading.Barrier(5)

for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()


