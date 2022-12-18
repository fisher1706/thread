# https://www.youtube.com/watch?v=Hsg3RrxEG9U&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=11
import multiprocessing
from multiprocessing import Pipe


def send_data(conn):
    conn.send("Hello world")
    conn.close()


if __name__ == '__main__':
    output_c, input_c = Pipe()
    p = multiprocessing.Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print("data:", output_c.recv())


