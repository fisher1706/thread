# https://www.youtube.com/watch?v=hAQb-HbkL8Y&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=4
import time
import threading

data = threading.local()

def get_name():
    print(data.name)

def t1():
    data.name = threading.currentThread().name
    get_name()

def t2():
    data.name = threading.currentThread().name
    get_name()


threading.Thread(target=t1, name="t1").start()
threading.Thread(target=t2, name="t2").start()





