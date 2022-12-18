import time
import multiprocessing


def test():
    while True:
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)


time.sleep(3)
pr = multiprocessing.Process(target=test, name="prc-1")
pr.start()

print("Proces start")
print(pr.is_alive())
print(pr.pid)

time.sleep(5)
pr.terminate()