import random
def sort(a=[]):
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (a[j] > a[j + 1]):
                p=a[j]
                a[j]=a[j+1]
                a[j+1]=p
    return a
a=[random.randint(0,1000) for i in range(100)]
print("unsorted array")
print(a)
a=sort(a)
print("Sorted array")
print(a)

