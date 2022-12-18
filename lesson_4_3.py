# https://www.youtube.com/watch?v=hAQb-HbkL8Y&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=4
import time
import threading

data = threading.local()

def get():
    print(data.value)

def t1():
    data.value = 111
    get()

def t2():
    data.value = 222
    get()


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()





