# Gries and Misra sieve — O(n)
def sieve(n):
    lp = (n+1)*[0]
    pr = []
    for i in range(2, n+1):
        if (lp[i] == 0):
            lp[i] = i
            pr.append(i)
        j = 0
        while (j < len(pr) and pr[j]<=lp[i] and i*pr[j]<=n):
            lp[i*pr[j]]=pr[j]
            j += 1
    return pr

assert sieve(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
