from bisect import bisect_right

# O(n^2)
def longest_increasing_subseg(a):
    n=len(a)
    d=n*[1]
    p=n*[-1]
    for i in range(n):
        for j in range(i):
            if a[j]<a[i]:
                if 1+d[j]>d[i]:
                    d[i]=1+d[j]
                    p[i]=j
    ans,pos=d[0],0
    for i in range(n):
        if d[i]>ans:
            ans=d[i]
            pos=i
    path=[]
    while pos!=-1:
        path.append(pos)
        pos=p[pos]
    path.reverse()
    return path

assert longest_increasing_subseg([6,5,3,2,1,2,1,2,5])==[4, 5, 8]

# O(n^2)
def longest_increasing_subseg_2(a):
    n=len(a)
    d=[]
    d.append(float('-inf'))
    for i in range(1,n+1):
        d.append(float('inf'))

    for i in range(n):
        for j in range(1,n+1):
            if d[j-1]<a[i] and a[i]<d[j]:
                d[j]=a[i]

    return len(filter(lambda n: n not in [float('inf'), float('-inf')], d))

assert longest_increasing_subseg_2([6,5,3,2,1,2,1,2,5])==3

# O(n*log n)
def longest_increasing_subseg_log(a):
    n=len(a)
    d=[0]
    for i in range(1,n+1):
        d.append(float('inf'))

    for i in range(n):
        x=bisect_right(d,a[i])
        j=int(x-d[0])
        if d[j-1]<a[i] and a[i]<d[j]:
            d[j]=a[i]

    return len(filter(lambda n: n not in [float('inf'),0], d))

assert longest_increasing_subseg_log([6,5,3,2,1,2,1,2,5])==3
