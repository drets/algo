def merge(A,p,q,r):
    L=A[p:q+1]
    L.append(float('inf'))
    R=A[q+1:r+1]
    R.append(float('inf'))
    i=j=0
    for k in range(p,r):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

A=[1,10,100,1000,10000,2,5,200,500,20000]
merge(A,0,4,9)
assert A == [1,2,5,10,100,200,500,1000,10000,20000]
