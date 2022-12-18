# https://www.youtube.com/watch?v=LddlE3n00W8&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=8
import multiprocessing


def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] - value: {value}\n")
    return value

def end_func(response):
    print('Task completed')
    print(f'response: {response}')



if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        # p.map(get_value, list(range(100)))
        p.map_async(get_value, list(range(100)), callback=end_func)
        p.close()
        p.join()






