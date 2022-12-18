# https://www.youtube.com/watch?v=PYizQpjCOTc&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=9
import time
from multiprocessing import Condition, Process


cond = Condition()


def f1():
    while True:
        with cond:
            cond.wait()
            print("Get event")


def f2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)


Process(target=f1).start()
Process(target=f2).start()

