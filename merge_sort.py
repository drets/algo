from math import floor

def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=(n1+1)*[float('inf')]
    R=(n2+1)*[float('inf')]
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+j+1]
    i=j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

B=[1,10,100,1000,10000,2,5,200,500,20000]
merge(B,0,4,9)
assert B == [1,2,5,10,100,200,500,1000,10000,20000]
C=[1,9,10,2,3]
merge(C,0,2,4)
assert C == [1,2,3,9,10], C
D=[1,9,2,50,100]
merge(D,0,1,4)
assert D == [1,2,9,50,100]
E=[50,7,1,5,6,1,9,10,2,3]
merge(E,5,7,9)
assert E == [50, 7, 1, 5, 6, 1, 2, 3, 9, 10]

def merge_sort(A,p,r):
    if p<r:
        q=floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

E=[10000,1000,100,10,1,2,5,200,500,20000]
merge_sort(E,0,9)
assert E == [1,2,5,10,100,200,500,1000,10000,20000]
