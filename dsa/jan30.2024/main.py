import time
import os

benchmarks = ['Benchmark-1.txt', 'Benchmark-2.txt', 'Benchmark-3.txt']

def p(s):
    print(s)
    with open('output.txt', 'a') as f:
        f.write(s + '\n')

def bubble_sort(l, benchmark):
    p("Bubble Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    for i in range(len(l)):
        print(i, i/len(l)*100)
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
    end = time.time()
    p(str(end - start))
    return l

def insertion_sort(l, benchmark):
    p("Insertion Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    for i in range(1, len(l)):
        print(i, i/len(l)*100)
        j = i - 1
        while j >= 0 and l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            j -= 1
    end = time.time()
    p(str(end - start))
    return l

def selection_sort(l, benchmark):
    p("Selection Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    for i in range(len(l)):
        print(i, i/len(l)*100)
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    end = time.time()
    p(str(end - start))
    return l

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    bubble_sort(l[:100], benchmark)
    bubble_sort(l[:1000], benchmark)
    bubble_sort(l[:5000], benchmark)
   

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    insertion_sort(l[:100], benchmark)
    insertion_sort(l[:1000], benchmark)
    insertion_sort(l[:5000], benchmark)
    

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    selection_sort(l[:100], benchmark)
    selection_sort(l[:1000], benchmark)
    selection_sort(l[:5000], benchmark)