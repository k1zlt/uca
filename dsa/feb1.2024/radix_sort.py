def counting_sort(l, place):
    size  = len(l)
    output = 

def radix_sort(l):
    m = max(l)
    place = 1
    while m // place > 0:
        counting_sort(l, place)
        place *= 10
