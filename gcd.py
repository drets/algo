def gcd_rec(a,b):
    if b==0:
        return a
    else:
        return gcd_rec(b,a%b)

def gcd(a,b):
    while b:
        a %= b
        a, b = b, a
    return a

assert gcd(12,9) == gcd_rec(12,9) == 3
