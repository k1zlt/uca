import time
import os

benchmarks = ['Benchmark-1.txt', 'Benchmark-2.txt', 'Benchmark-3.txt']

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    start = time.time()
    print("start")
    bubble_sort(l)
    end = time.time()
    print()
    print(benchmark, end - start)