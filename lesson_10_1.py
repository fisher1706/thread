import multiprocessing
import random
from multiprocessing import Process, Barrier


b = Barrier(5)

def f1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2, 10)
    print(f"[{name}] - sleep {sl} seconds")
    bar.wait()
    print(f"[{name}] - start")


for i in range(8):
    Process(target=f1, args=(b,)).start()
