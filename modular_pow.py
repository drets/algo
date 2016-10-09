def bin_modular_pow(a, n, m):
    res = 1
    while n:
        if (n & 1):
            res = (a*res)%m
        a = (a*a)%m
        n >>= 1
    return res

print(bin_modular_pow(3,pow(10,100), 4*(pow(5,14)))
#3574218752
#2^(3^(10^100))
