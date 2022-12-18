# https://www.youtube.com/watch?v=LddlE3n00W8&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=8
import multiprocessing


def end_func(response):
    print(f'end_func: {response}\n')


def out(x, y, z):
    print(f'value: {x} {y} {z}\n')
    return x, y, z




if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)

        p.close()
        p.join()
