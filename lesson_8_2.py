# https://www.youtube.com/watch?v=LddlE3n00W8&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=8
import multiprocessing


def out(x):
    print(f'value: {x}\n')
    return x

def end_func(response):
    print(f'end_func: {response}\n')



if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func)
        p.close()
        p.join()
