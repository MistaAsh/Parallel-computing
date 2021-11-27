import multiprocessing as mp
import math
import time

def array_sum(arr):
    return sum(arr)

if __name__ == '__main__':
    t = int(input('Enter the number of testcases: '))

    for _ in range(t):
        n = int(input('\nEnter the number of elements: '))
        print('Enter array: ', end='')
        arr = list(map(int, input().split()))

        t1 = time.time()

        k = 4   #'4' can be replace with any number of processes you'd want to create (>0)
        slice = math.ceil((n/k) * k)

        p = mp.Pool()
        res = p.map(array_sum, [arr[i*slice: min(n, (i+1)*slice)] for i in range(k)])

        p.close()
        p.join()

        print(f'\nPool sum = {sum(res)} \t{time.time() - t1}')


        t2 = time.time()
        print(f'Direct sum = {sum(arr)} \t {time.time()-t2}')