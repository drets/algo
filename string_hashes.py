def hash(s):
    p=31
    hash,p_pow=0,1
    for i in range(len(s)):
        hash=(ord(s[i])-ord('a')+1)*p_pow
        p_pow*=p
    return hash

def find_the_same_strings(xs):
    p=31
    n=len(xs)
    p_pow=[1]
    for i in range(1,10000):
        p_pow.append(p_pow[i-1]*p)
    hashes=[]
    for i in range(n):
        hash=0
        for j in range(len(xs[i])):
            hash+=(ord(xs[i][j])-ord('a')+1)*p_pow[j]
        hashes.append((hash,i))
    hashes.sort()
    res=[]
    i,j=1,0
    while True:
        if i>=n:
            res.insert(0,list(map(lambda tpl : tpl[1], hashes[j:i])))
            break
        if hashes[i][0]!=hashes[j][0]:
            res.append(list(map(lambda tpl : tpl[1], hashes[j:i])))
            j=i
        i+=1
    return res

assert find_the_same_strings(['a','100','a','100','3','hello','hello','hello']) == [[5, 6, 7], [1, 3], [4], [0, 2]]

def substrings_equal(s,i1,i2,length):
    p=31
    l=len(s)
    p_pow=[1]
    for i in range(1,l):
        p_pow.append(p_pow[i-1]*p)
    h=[]
    for i in range(l):
        h.append((ord(s[i])-ord('a')+1)*p_pow[i])
        if i:
            h[i]+=h[i-1]
    h1=h[i1+length-1]
    if i1:
        h1-=h[i1-1]
    h2=h[i2+length-1]
    if i2:
        h2-=h[i2-1]
    return i1<i2 and h1*p_pow[i2-i1]==h2 or \
        i1>i2 and h1==h2*p_pow[i1-i2]

assert substrings_equal("abcabc",0,3,3)
assert substrings_equal("abceabc",0,4,3)
assert not substrings_equal("abcabce",0,4,3)

def count_substrings(s):
    n=len(s)
    p=31
    p_pow=[1]
    for i in range(1,n):
        p_pow.append(p_pow[i-1]*p)
    h=[]
    for i in range(n):
        h.append((ord(s[i])-ord('a')+1)*p_pow[i])
        if i:
            h[i]+=h[i-1]
    result=0
    for l in range(1,n+1):
        hs=[]
        for i in range(n-l+1):
            cur_h=h[i+l-1]
            if i:
                cur_h-=h[i-1]
            cur_h*=p_pow[n-i-1]
            hs.append(cur_h)
        hs.sort()
        result+=len(set(hs))
    return result

assert count_substrings("abc") == 6
assert count_substrings("ab")  == 3
assert count_substrings("a")   == 1
