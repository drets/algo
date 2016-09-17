from gcd import gcd

def lcm(a,b):
    return a / gcd(a,b) * b

assert lcm(16,20) == 80
