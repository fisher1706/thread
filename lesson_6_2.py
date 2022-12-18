import time
import multiprocessing


def test():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)

prc = []

for _ in range(3):
    pr = multiprocessing.Process(target=test, name="prc-1")
    prc.append(pr)
    pr.start()


for i in prc:
    i.join()

print("All process stop")

