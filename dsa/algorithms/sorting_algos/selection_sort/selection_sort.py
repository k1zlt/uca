l = [23, 242, 1, 3, 123, 123, 4, 2, 2342, 3423, 4234, 2342, 3423]

def selection_sort(l):
    for i in range(len(l)):
        temp = i
        for j in range(i, len(l)):
            if l[temp] > l[j]:
                temp = j
        l[temp], l[i] = l[i], l[temp]
    return l

print(selection_sort(l))