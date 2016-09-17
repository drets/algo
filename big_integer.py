def output(a):
    if a:
        print(a.pop(),end="")
    else:
        print(0)
    i=len(a)-1
    while i>=0:
        print("%09d" % a[i],end="")
        i-=1

def read(s):
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
