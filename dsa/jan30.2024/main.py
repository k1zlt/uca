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

def merge_sort2(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        merge_sort2(left)
        merge_sort2(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              l[k] = left[i]
              i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    return l

def merge_sort(l, benchmark):
    p("Merge Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        merge_sort2(left)
        merge_sort2(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              l[k] = left[i]
              i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    end = time.time()
    p(str(end - start))
    return l

def partition(l, low, high):
    i = low - 1
    pivot = l[high]
    for j in range(low, high):
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i + 1], l[high] = l[high], l[i + 1]
    return i + 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))

            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

    return arr

def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(l, benchmark):
    p("Quick Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    quicksort(l)
    end = time.time()
    p(str(end - start))
    return l

def counting_sort(l, benchmark):
    p("Counting Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    max_element = max(l)
    min_element = min(l)
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(l))]
    for i in range(0, len(l)):
        count_arr[l[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(l) - 1, -1, -1):
        output_arr[count_arr[l[i] - min_element] - 1] = l[i]
        count_arr[l[i] - min_element] -= 1
    for i in range(0, len(l)):
        l[i] = output_arr[i]
    end = time.time()
    p(str(end - start))
    return l

def counting_sort2(l, exp):
    n = len(l)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = l[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = l[i] // exp
        output[count[index % 10] - 1] = l[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(l)):
        l[i] = output[i]

def redix_sort(l, benchmark):
    p("Redix Sort for " + benchmark + " Length of list: " + str(len(l)))
    start = time.time()
    max_element = max(l)
    exp = 1
    while max_element // exp > 0:
        counting_sort2(l, exp)
        exp *= 10
    end = time.time()
    p(str(end - start))
    return l


for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    bubble_sort(l[:100], benchmark)
    bubble_sort(l[:1000], benchmark)
    bubble_sort(l[:5000], benchmark)
    bubble_sort(l[:10000], benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    insertion_sort(l[:100], benchmark)
    insertion_sort(l[:1000], benchmark)
    insertion_sort(l[:5000], benchmark)
    insertion_sort(l[:10000], benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    selection_sort(l[:100], benchmark)
    selection_sort(l[:1000], benchmark)
    selection_sort(l[:5000], benchmark)
    selection_sort(l[:10000], benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    merge_sort(l[:100], benchmark)
    merge_sort(l[:1000], benchmark)
    merge_sort(l[:5000], benchmark)
    merge_sort(l[:10000], benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    quick_sort(l[:100], benchmark)
    quick_sort(l[:1000], benchmark)
    quick_sort(l[:5000], benchmark)
    quick_sort(l[:10000], benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    redix_sort(l[:100], benchmark)
    redix_sort(l[:1000], benchmark)
    redix_sort(l[:5000], benchmark)
    redix_sort(l[:10000], benchmark)
    redix_sort(l, benchmark)

for benchmark in benchmarks:
    l = list(map(int, open(os.path.join(os.getcwd(), 'benchmarks', benchmark), 'r').readlines()))
    counting_sort(l[:100], benchmark)
    counting_sort(l[:1000], benchmark)
    counting_sort(l[:5000], benchmark)
    counting_sort(l[:10000], benchmark)
    counting_sort(l, benchmark)

