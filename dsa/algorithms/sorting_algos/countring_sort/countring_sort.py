def countring_sort(arr):
    max_num = max(arr)
    min_num = min(arr)

    countarray = [0] * (max_num - min_num + 1)
    for i in arr:
        countarray[i - min_num] += 1

    k = 0
    for i in range(max_num - min_num + 1):
        while countarray[i] > 0:
            countarray[i] -= 1
            arr[k] = i + min_num
            k += 1

    return arr

arr = [4, 23, 11, 33, 23, 23, 23, 1, 1, 2, 32, 32, 32, 32, 1, 2]
print(countring_sort(arr.copy()))
arr.sort()
print(arr)
