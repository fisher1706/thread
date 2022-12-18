# https://www.youtube.com/watch?v=PYizQpjCOTc&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=9
import time
from multiprocessing import Process, Event


event = Event()


def test():
    print("func start")
    while True:
        event.wait()
        print("test")
        time.sleep(1)


def test_event():
    while True:
        time.sleep(2)
        event.set()
        print("Event True")
        time.sleep(2)
        event.clear()
        print("Event False")

Process(target=test).start()
Process(target=test_event).start()