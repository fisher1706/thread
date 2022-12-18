# https://www.youtube.com/watch?v=Bpu3VxfBrqY&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=3

import time
import threading

value = 0
locker = threading.Lock()


# def inc_value():
#     global value
#     while True:
#         locker.acquire()
#         value += 1
#         time.sleep(1)
#         print(value)
#         locker.release()

def inc_value():
    global value
    while True:
        with locker:
            value += 1
            time.sleep(1)
            print(value)


for _ in range(5):
    thr = threading.Thread(target=inc_value).start()
