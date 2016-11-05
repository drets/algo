# O(n log n)
def quick_sort(lst):
    if len(lst) == 0:
        return lst

    less = []
    greater = []
    equal = []
    pivot = lst[0]
    for x in lst:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)

assert quick_sort([12,3,4,5,7,1,17]) == [1, 3, 4, 5, 7, 12, 17]

def partition(lst,l,r):
    pivot=l
    for i in range(l+1,r+1):
        if lst[i] <= lst[l]:
            pivot += 1
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[l] = lst[l], lst[pivot]
    return pivot

def quick_sort_inplace(lst,l=0,r=None):
    if r is None:
        r=len(lst)-1
    if l >= r:
        return
    pivot=partition(lst,l,r)
    quick_sort_inplace(lst,l,pivot-1)
    quick_sort_inplace(lst,pivot+1,r)

A = [6,5,4,3,2,1]
quick_sort_inplace(A)
assert A == [1,2,3,4,5,6]
