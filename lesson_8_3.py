# https://www.youtube.com/watch?v=LddlE3n00W8&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=8
import multiprocessing


def out(x, y, z):
    print(f'value: {x} {y} {z}\n')




if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.starmap(out, [(1, 2, 3), (4, 5, 6)])

        p.close()
        p.join()
