from math import floor

def binary_search_rec(a,t):
    def binary_search_rec(a,t,l,r):
        if (l>r):
            return -1
        m = floor((l+r)/2)
        if a[m]==t:
            return m
        elif a[m]>t:
            return binary_search_rec(a,t,l,m-1)
        elif a[m]<t:
            return binary_search_rec(a,t,m+1,r)
    return binary_search_rec(a,t,0,len(a)-1)

def binary_search(a,t):
    l = 0
    r = len(a) - 1
    while l<=r:
        m = floor((l+r)/2)
        if a[m]==t:
            return m
        elif a[m]>t:
            r=m-1
        elif a[m]<t:
            l=m+1
    return -1

lst = [1,3,5,7,9,11]
lst.sort()

assert binary_search_rec(lst, -11) == binary_search(lst, -11) == -1
assert binary_search_rec(lst, 0) == binary_search(lst, 0) == -1
assert binary_search_rec(lst, 6) == binary_search(lst, 6) == -1
assert binary_search_rec(lst, 10000000000000000000000000000000000) == binary_search(lst, 10000000000000000000000000000000000) == -1
assert binary_search_rec(lst, -10000000000000000000000000000000000) == binary_search(lst, -10000000000000000000000000000000000) == -1

assert binary_search_rec(lst, 1) == binary_search(lst, 1) == 0
assert binary_search_rec(lst, 3) == binary_search(lst, 3) == 1
assert binary_search_rec(lst, 5) == binary_search(lst, 5) == 2
assert binary_search_rec(lst, 7) == binary_search(lst, 7) == 3
assert binary_search_rec(lst, 9) == binary_search(lst, 9) == 4
assert binary_search_rec(lst, 11) == binary_search(lst, 11) == 5
