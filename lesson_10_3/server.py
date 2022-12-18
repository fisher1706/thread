from multiprocessing.managers import BaseManager
import time


def get_time():
    return time.time()


BaseManager.register("get", callable=get_time)
manager = BaseManager(address=('', 4444), authkey=b'abc')
server = manager.get_server()
print("server_start")
server.serve_forever()





