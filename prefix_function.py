# O(n^3)
def prefix_function(s):
    n=len(s)
    pi=n*[0]
    for i in range(n):
        for k in range(i+1):
            if s[0:k] == s[i-k+1:i+1]:
                pi[i]=k
    return pi

assert prefix_function("abcabcd") == [0, 0, 0, 1, 2, 3, 0]
assert prefix_function("aabaaab") == [0, 1, 0, 1, 2, 2, 3]

# O(n)
def kmp_prefix_function(s):
    n=len(s)
    pi=n*[0]
    for i in range(1,n):
        j=pi[i-1]
        while j>0 and s[i]!=s[j]:
            j=pi[j-1]
        if s[i]==s[j]:
            j+=1
        pi[i]=j
    return pi

assert kmp_prefix_function("abcabcd") == [0, 0, 0, 1, 2, 3, 0]
assert kmp_prefix_function("aabaaab") == [0, 1, 0, 1, 2, 2, 3]
