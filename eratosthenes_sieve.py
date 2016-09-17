# O(n log log n)
def sieve(n):
    assert n > 1
    prime = (n+1) * [True]
    prime[0] = prime[1] = False
    for i in range(2,n+1):
        if prime[i]:
            if i*i <= n:
                for j in range(i*i, n+1, i):
                    prime[j] = False
    return [i for i, x in enumerate(prime) if x]

assert sieve(10) == [2,3,5,7]
