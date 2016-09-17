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
