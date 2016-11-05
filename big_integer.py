def from_bi(a):
    res=''
    b=list(a)
    if b:
        res=str(b.pop())
    else:
        res='0'
    i=len(b)-1
    while i>=0:
        res+=str('{:>09}'.format(b[i]))
        i-=1
    return res

def to_bi(s):
    a=[]
    i=len(s)
    while i>0:
        if i<9:
            a.append(int(s[0:i]))
        else:
            p=i-9
            a.append(int(s[p:i]))
        i-=9
    clean_zeros(a)
    return a

def clean_zeros(a):
    while len(a)>1 and a[-1]==0:
        a.pop()

s=1234567891011121314151617181920212223242526272829303132333343536373839404142
a=to_bi(str(s))

assert a==[839404142, 343536373, 303132333, 526272829, 212223242, 617181920, 121314151, 567891011, 1234]
assert from_bi(a)==str(s)

def add(a,b):
    base=1000*1000*1000
    carry=0
    i=0
    while i<max(len(a), len(b)) or carry:
        if i==len(a):
            a.append(0)
        a[i]+=carry+(b[i] if i<len(b) else 0)
        if a[i]>=base:
            a[i]-=base
            carry=1
        else:
            carry=0
        i+=1
    return a

assert str(s+s)==from_bi(add(to_bi(str(s)),to_bi(str(s))))

def subtract(a,b):
    if len(a)==len(b):
        assert a[-1]>=b[-1]
    else:
        assert len(a)>len(b)

    base=1000*1000*1000
    carry=0
    i=0
    while i<len(b) or carry:
        a[i]-=carry+(b[i] if i < len(b) else 0)
        if a[i]<0:
            a[i]+=base
            carry=1
        else:
            carry=0
        i+=1
    clean_zeros(a)
    return a

m=4140393837363534333231302928272625242322212019181716151413121110987654321
assert str(s-m)==from_bi(subtract(to_bi(str(s)),to_bi(str(m))))

def multiply_on_short(a,b):
    base=1000*1000*1000
    assert b<base
    carry=0
    i=0
    while i<len(a) or carry:
        if i==len(a):
            a.append(0)
        cur=carry + a[i]*b
        a[i]=int(cur%base)
        carry=int(cur/base)
        i+=1
    clean_zeros(a)
    return a

n=3
assert str(s*n)==from_bi(multiply_on_short(to_bi(str(s)),n))

def multiply(a,b):
    base=1000*1000*1000
    c=(len(a)+len(b))*[0]
    for i in range(len(a)):
        carry=j=0
        while j<len(b) or carry:
            cur=c[i+j]+a[i]*(b[j] if j<len(b) else 0)+carry
            c[i+j]=int(cur%base)
            carry=int(cur/base)
            j+=1
    clean_zeros(c)
    return c

assert str(m*s)==from_bi(multiply(to_bi(str(m)),to_bi(str(s))))

def devide_on_short(a,b):
    base=1000*1000*1000
    assert b<base
    carry=0
    i=len(a)-1
    while i>=0:
        cur=a[i]+carry*base
        a[i]=int(cur/b)
        carry=int(cur%b)
        i-=1
    clean_zeros(a)
    return a

h=411522630337040438050539060640070741080842090943101044111114512124613134714 # s/n
assert str(h)==from_bi(devide_on_short(to_bi(str(s)),n))
