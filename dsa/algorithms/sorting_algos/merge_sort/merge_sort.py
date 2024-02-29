def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i = 0
    j = 0
    k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        k += 1
        i += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    

arr = [2, 1, 2, 1, 2, 5, 4, 3, 2, 5, 3, 2, 1, 5, 7, 22, 72, 7, 2, 1, 6, 3, 5, 3, 5]
merge_sort(arr)
print(arr)