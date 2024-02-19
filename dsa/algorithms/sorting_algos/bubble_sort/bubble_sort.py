l = [3, 22, 213, 5, 3, 1, 2, 1, 2, 1, 2, 14, 12]

def bubble_sort(l):
    for i in range(len(l)-1, 1, -1):
        for j in range(i):
            if l[i] < l[j]: l[i], l[j] = l[j], l[i]
    return l

print(bubble_sort(l))
