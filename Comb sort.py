import random
import math
def getNextGap(gap):
    gap = gap/1.25
    gap=math.floor(gap)
    if gap < 1:
        return 1
    return gap
def sort(arr=[]):
    n = len(arr)
    gap = n
    swapped = True
    while gap !=1 or swapped == 1:
        swapped = False
        gap = getNextGap(gap)
        for i in range(0, n-gap):            
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]                
                swapped = True
    return a
a=[random.randint(0,10000) for i in range(50000)]
print("unsorted array")
print(a)
a=sort(a)
print("Sorted array")
print(a)
