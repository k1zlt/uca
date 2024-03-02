from functools import reduce

def radix_sort(arr):
    num_digits = len(str(max(arr)))

    for digit in range(num_digits):
        buckets = [[] for x in range(10)]
        for i in arr:
            buckets[i // 10 ** digit % 10].append(i)

        arr = reduce(lambda x, y: x + y, buckets)

    return arr


arr = [12, 452, 1, 51, 15, 151, 511, 5, 51, 141, 15, 151, 513, 12, 1352]
print(radix_sort(arr))