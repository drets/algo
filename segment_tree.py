import bisect
# O(log n)

def build(a,v,tl,tr):
    if tl==tr:
        t[v]=a[tl]
    else:
        tm=int((tl+tr)/2)
        build(a,v*2,tl,tm)
        build(a,v*2+1,tm+1,tr)
        t[v]=t[v*2]+t[v*2+1]

def sum(v,tl,tr,l,r):
    if l>r:
        return 0
    if l==tl and r==tr:
        return t[v]
    tm=int((tl+tr)/2)
    return sum(v*2,tl,tm,l,min(r,tm)) + \
        sum(v*2+1,tm+1,tr,max(l,tm+1),r)

def update(v,tl,tr,pos,new_val):
    if tl==tr:
        t[v]=new_val
    else:
        tm=int((tl+tr)/2)
        if pos<=tm:
            update(v*2,tl,tm,pos,new_val)
        else:
            update(v*2+1,tm+1,tr,pos,new_val)
        t[v]=t[v*2]+t[v*2+1]

a=[1,2,3,4,5,6,7,8,9]
n=len(a)
t=4*n*[None]
build(a,1,0,n-1)

assert sum(1,0,n-1,3,5)==15 # 4,5,6

update(1,0,n-1,4,100)
assert sum(1,0,n-1,3,5)==110 # 4,100,6

# Extended segment tree.

def combine2(a,b):
    (a1,a2)=a
    (b1,b2)=b
    if a1>b1:
        return a
    if b1>a1:
        return b
    return (a1,a2+b2)

def build2(a,v,tl,tr):
    if tl==tr:
        t[v]=(a[tl],1)
    else:
        tm=int((tl+tr)/2)
        build2(a,v*2,tl,tm)
        build2(a,v*2+1,tm+1,tr)
        t[v]=combine2(t[v*2],t[v*2+1])

def get_max2(v,tl,tr,l,r):
    if l>r:
        return (float('-inf'),0)
    if l==tl and r==tr:
        return t[v]
    tm=int((tl+tr)/2)
    return combine2(
        get_max2(v*2,tl,tm,l,min(r,tm)),
        get_max2(v*2+1,tm+1,tr,max(l,tm+1),r)
    )

def update2(v,tl,tr,pos,new_val):
    if tl==tr:
        t[v]=(new_val,1)
    else:
        tm=int((tl+tr)/2)
        if pos<=tm:
            update2(v*2,tl,tm,pos,new_val)
        else:
            update2(v*2+1,tm+1,tr,pos,new_val)
        t[v]=combine2(t[v*2],t[v*2+1])

a=[1,2,3,4,6,5,6,7,8,9,0]
n=len(a)
t=4*n*[None]
build2(a,1,0,n-1)

assert get_max2(1,0,n-1,3,6)==(6,2) # 4,6,5,6

update2(1,0,n-1,6,7)==(7,1)
assert get_max2(1,0,n-1,3,6)==(7,1) # 4,6,5,7

# Find segment with max sum

class data(object):
    def __init__(self,sum,pref,suff,ans):
        self.sum = sum
        self.pref = pref
        self.suff = suff
        self.ans = ans

def combine3(l,r):
    return data(
        l.sum+r.sum,
        max(l.pref,l.sum+r.pref),
        max(r.suff,r.sum+l.suff),
        max(max(l.ans,r.ans),l.suff+r.pref)
    )

def make_data3(val):
    return data(
        val,
        max(0,val),
        max(0,val),
        max(0,val)
    )

def build3(a,v,tl,tr):
    if tl==tr:
        t[v]=make_data3(a[tl])
    else:
        tm=int((tl+tr)/2)
        build3(a,v*2,tl,tm)
        build3(a,v*2+1,tm+1,tr)
        t[v]=combine3(t[v*2],t[v*2+1])

def update3(v,tl,tr,pos,new_val):
    if tl==tr:
        t[v]=make_data3(new_val)
    else:
        tm=int((tl+tr)/2)
        if pos<=tm:
            update3(v*2,tl,tm,pos,new_val)
        else:
            update3(v*2+1,tm+1,tr,pos,new_val)
        t[v]=combine3(t[v*2],t[v*2+1])

def query3(v,tl,tr,l,r):
    if l==tl and tr==r:
        return t[v]
    tm=int((tl+tr)/2)
    if r<=tm:
        return query3(v*2,tl,tm,l,r)
    if l>tm:
        return query3(v*2+1,tm+1,tr,l,r)
    return combine3(
        query3(v*2,tl,tm,l,tm),
        query3(v*2+1,tm+1,tr,tm+1,r)
    )

a=[1,2,-100,7,7,6,-100,3,4,5,1]
n=len(a)
t=4*n*[None]
build3(a,1,0,n-1)

assert query3(1,0,n-1,0,n-1).ans == 20

update3(1,0,n-1,0,40)
assert query3(1,0,n-1,0,n-1).ans == 42

# Find min number which is bigger or equal to given number in given segment.

def build4(a,v,tl,tr):
    if tl==tr:
        t[v]=[1,a[tl]]
    else:
        tm=int((tl+tr)/2)
        build4(a,v*2,tl,tm)
        build4(a,v*2+1,tm+1,tr)
        t[v]=sorted(t[v*2]+t[v*2+1])

# O(log^2 n)
def query4(v,tl,tr,l,r,x):
    if l>r:
        return float('inf')
    if l==tl and r==tr:
        pos=bisect.bisect_left(t[v],x)
        if pos!=t[v][-1]:
            return t[v][pos]
        return float('inf')
    tm=int((tl+tm)/2)
    return min3(
        query4(v*2,tl,tm,l,min(r,tm),x3),
        query4(v*2+1,tm+1,tr,max(l,tm+1),r,x)
    )


a=[1,2,-100,7,7,42,6,-100,3,4,9,100,1000,5,1]
n=len(a)
t=4*n*[None]
build4(a,1,0,n-1)

assert query4(1,0,n-1,0,n-1,42) == 42

# Summing on the segment

def build5(a,v,tl,tr):
    if tl==tr:
        t[v]=a[tl]
    else:
        tm=int((tl+tr)/2)
        build5(a,v*2,tl,tm)
        build5(a,v*2+1,tm+1,tr)

def update5(v,tl,tr,l,r,add):
    if l>r:
        return
    if l==r and tr==r:
        t[v]+=add
    else:
        tm=int((tl+tr)/2)
        update5(v*2,tl,tm,l,min(r,tm),add)
        update5(v*2+1,tm+1,tr,max(l,tm+1),r,add)

def get5(v,tl,tr,pos):
    if tl==tr:
        return t[v]
    tm=int((tl+tr)/2)
    if pos<=tm:
        return t[v]+get5(v*2,tl,tm,pos)
    else:
        return t[v]+get5(v*2+1,tm+1,tr,pos)

a=[1,2,-100,7,7,42,6,-100,3,4,9,100,1000,5,1]
n=len(a)
t=4*n*[0]
build5(a,1,0,n-1)

assert get5(1,0,n-1,4) == 7
assert get5(1,0,n-1,5) == 42
assert get5(1,0,n-1,6) == 6

update5(1,0,n-1,4,5,1) == 1

assert get5(1,0,n-1,4) == 8
assert get5(1,0,n-1,5) == 43
assert get5(1,0,n-1,6) == 6

# Setting on the segment

def push6(v):
    if t[v]!=-1:
        t[v*2]=t[v*2+1]=t[v]
        t[v]=-1

def update6(v,tl,tr,l,r,color):
    if l>r:
        return
    if l==tl and r==tr:
        t[v]=color
    else:
        push6(v)
        tm=int((tl+tr)/2)
        update6(v*2,tl,tm,l,min(r,tm),color)
        update6(v*2+1,tm+1,tr,max(l,tm+1),r,color)

def get6(v,tl,tr,pos):
    if tl==tr:
        return t[v]
    push6(v)
    tm=int((tl+tr)/2)
    if pos<=tm:
        return get6(v*2,tl,tm,pos)
    else:
        return get6(v*2+1,tm+1,tr,pos)


a=[1,2,-100,7,7,42,6,-100,3,4,9,100,1000,5,1]
n=len(a)
t=4*n*[-1]

build5(a,1,0,n-1)
assert get6(1,0,n-1,1)==2

update6(1,0,n-1,1,2,3)
assert get6(1,0,n-1,0)==1
assert get6(1,0,n-1,1)==3
assert get6(1,0,n-1,2)==3
assert get6(1,0,n-1,3)==7
