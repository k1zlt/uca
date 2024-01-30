import time
import os

benchmarks = ['Benchmark-1.txt', 'Benchmark-2.txt', 'Benchmark-3.txt']

def p(s):
    print(s)
    with open('output.txt', 'a') as f:
        f.write(s + '\n')

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        while j >= 0 and l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            j -= 1
    return l

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
    p("Bubble Sort for " + benchmark)
    p("Length of list: " + str(len(l)))
    start = time.time()
    bubble_sort(l)
    end = time.time()
    p(benchmark + " " + str(end - start))

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    p("Insertion Sort for " + benchmark)
    p("Length of list: " + str(len(l)))
    start = time.time()
    insertion_sort(l)
    end = time.time()
    p(benchmark + " " + str(end - start))

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    p("Selection Sort for " + benchmark)
    p("Length of list: " + str(len(l)))
    start = time.time()
    selection_sort(l)
    end = time.time()
    p(benchmark + " " + str(end - start))