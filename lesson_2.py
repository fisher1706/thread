# https://www.youtube.com/watch?v=SQXQPIXXqQQ&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=2

import time
import threading


def get_data(data):
    for _ in range(5):
        print(f"{threading.current_thread().name} - {data}")
        time.sleep(1)


# thr = threading.Thread(target=get_data, args=(str(time.time()),))
thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
thr.start()
time.sleep(1)
print("finish")
