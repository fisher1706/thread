# https://www.youtube.com/watch?v=oA6m1J7FHKM&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=1&t=1s

import threading
import time


def get_data(data, value):
    for _ in range(value):
        print(f"[{threading.current_thread().name} {data}]")
        time.sleep(5)

thr_list = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f"thr-{i}")
    thr_list.append(thr)
    thr.start()

# print("thr_list:", thr_list)

for i in thr_list:
    i.join()


print("finish")

