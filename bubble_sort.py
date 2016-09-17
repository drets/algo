# O(n^2)
def bubble_sort(a):
    while True:
        sorted=True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                sorted=False
        if sorted:
            break

A = [12,3,4,5,7,1,17]
bubble_sort(A)
assert A == [1, 3, 4, 5, 7, 12, 17]
