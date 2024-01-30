import time
import os

benchmarks = ['Benchmark-1.txt', 'Benchmark-2.txt', 'Benchmark-3.txt']

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    start = time.time()
    print("start")
    selection_sort(l)
    end = time.time()
    print()
    print(benchmark, end - start)