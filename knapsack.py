def memoize(f):
    class memodict(dict):
        def __init__(self,f):
            self.f=f
        def __call__(self,*args):
            return self[args]
        def __missing__(self,key):
            ret=self[key]=self.f(*key)
            return ret
    return memodict(f)

def knapsack(items,maxweight):
    @memoize
    def best_value(i,j):
        if i==0:
            return 0
        value,weight=items[i-1]
        if weight>j:
            return best_value(i-1,j)
        else:
            return max(best_value(i-1,j),
                       best_value(i-1,j-weight)+value)

    j=maxweight
    result=[]
    for i in range(len(items),0,-1):
        if best_value(i,j)!=best_value(i-1,j):
            result.append(items[i-1])
            j-=items[i-1][1]
    result.reverse()
    return best_value(len(items),maxweight),result

assert knapsack([(1,1),(2,1),(2,2),(10,4),(4,12)],15) == (15, [(1, 1), (2, 1), (2, 2), (10, 4)])
