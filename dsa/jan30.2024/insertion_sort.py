import time
import os

benchmarks = ['Benchmark-1.txt', 'Benchmark-2.txt', 'Benchmark-3.txt']

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        while j >= 0 and l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            j -= 1
    return l

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    start = time.time()
    print("start")
    insertion_sort(l)
    end = time.time()
    print()
    print(benchmark, end - start)