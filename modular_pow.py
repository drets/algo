def bin_modular_pow(a, n, m):
    res = 1
    while n:
        if (n & 1):
            res = (a*res)%m
        a = (a*a)%m
        n >>= 1
    return res

assert bin_modular_pow(2,pow(3,100),100000) == 58752
