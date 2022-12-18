# https://www.youtube.com/watch?v=oA6m1J7FHKM&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=1&t=1s

import threading
import time


def get_data(data):
    while True:
        print(f"[{threading.current_thread().name} {data}]")
        time.sleep(5)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1")
thr.start()


# for i in range(100):
#     print(f"current: {i}")
#     time.sleep(1)
#
#     if i % 10 == 0:
#         print("active thread:", threading.active_count())
#         print("enumerate:", threading.enumerate())
#         print("thr-1 is alive:", thr.is_alive())


print("name:", threading.main_thread().name)
threading.main_thread().setName("result")
print("result:", threading.main_thread().name)

