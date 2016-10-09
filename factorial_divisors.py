import math

def fact_pow(n,k):
  res=0
  while n:
    n = int(n/k)
    res += n
  return res

n,k = 100,3
assert math.factorial(n) % k**fact_pow(n,k) == 0
