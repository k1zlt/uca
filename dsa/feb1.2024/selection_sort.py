nums = [6, 4, 32, 5, 23,5 ,23 , 25,2, 34]

def selection_sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if (l[i] > l[j]):
                l[i], l[j] = l[j], l[i]

selection_sort(nums)
print(nums)