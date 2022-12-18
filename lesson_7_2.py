# https://www.youtube.com/watch?v=VhvD6ipuEX4&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=7&t=75s
import multiprocessing


lock = multiprocessing.RLock()


def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Process [{pr_name}] start')



multiprocessing.Process(target=get_value, args=(lock,)).start()
multiprocessing.Process(target=get_value, args=(lock,)).start()