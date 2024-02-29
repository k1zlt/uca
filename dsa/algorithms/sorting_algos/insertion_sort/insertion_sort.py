def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

    return arr

print(insertion_sort([12, 3, 2, 1, 2, 3, 4, 2, 1, 111, 222, 111, 22, 1.2]))