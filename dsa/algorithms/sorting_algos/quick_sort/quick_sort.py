def split(arr, pivot):
    lower = []
    upper = []
    for i in arr:
        if i < pivot:
            lower.append(i)
        else:
            upper.append(i)
    return lower, upper

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = split(arr[1:], pivot)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] + right

arr = [3, 5, 3, 2, 5, 1, 7, 5, 1, 4, 1, 4, 1, 5, 3, 1, 5, 3]
# arr = [1, 3, 2]
print(quick_sort(arr))
