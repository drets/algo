def noKill(x,y):
    return x[0] != y[0] and \
           x[1] != y[1] and \
          (x[0] - x[1] != y[0] - y[1]) and \
          (x[1] - x[0] != y[0] - y[1])

def dfs(x):
    if 8 == len(x):
        print(x)
    else:
        for y in range(8):
            nw = (len(x),y)
            if all(map(lambda ix: noKill(ix, nw), x)):
                x.append(nw)
                dfs(x)
                x.pop()

dfs([])
