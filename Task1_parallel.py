import multiprocessing as mp
import math

def array_sum(arr):
    total_sum.value += sum(arr)

t = int(input('Enter the number of testcases: '))

for _ in range(t):
    n = int(input('\nEnter the number of elements: '))
    print('Enter array: ', end='')
    arr = list(map(int, input().split()))

    total_sum = mp.Value('i', lock = False)
    total_sum.value = 0

    slice = math.ceil((n/4) * 4)
        
    processes = []
    for i in range(4):
        p = mp.Process(target = array_sum, args = [arr[i*slice: min(n, (i+1)*slice)]])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(total_sum.value)