def binpow_rec(a, n):
    if (n==0):
        return 1;
    elif (n % 2 == 1):
        return binpow_rec(a,n-1) * a
    else:
        b = binpow_rec(a, n/2)
        return b * b

def binpow(a, n):
    res = 1
    while n:
        if (n & 1):
            res *= a
            n -= 1
        else:
            a *= a
            n >>= 1
    return res

def binpow_2(a, n):
    res = 1
    while n:
        if (n & 1):
            res *= a
        a *= a
        n >>= 1
    return res

assert binpow_rec(2,12345) == binpow(2,12345) == binpow_2(2,12345)
