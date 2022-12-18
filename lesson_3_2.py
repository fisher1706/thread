# https://www.youtube.com/watch?v=Bpu3VxfBrqY&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=3

import time
import threading


value = 0
locker = threading.RLock()


def inc_value():
    print("Блокируем поток ...")
    locker.acquire()
    print("Поток разблокирован ...")


thr1 = threading.Thread(target=inc_value).start()
thr2 = threading.Thread(target=inc_value).start()

