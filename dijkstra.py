g = [ [(1,7),(2,9),(5,14)],
      [(0,7),(2,10),(3,15)],
      [(0,9),(1,10),(3,11),(5,2)],
      [(1,15),(2,11),(4,6)],
      [(3,6),(5,9)],
      [(0,14),(2,2),(4,9)]
    ] # https://upload.wikimedia.org/wikipedia/commons/d/de/Dijkstra_graph0.PNG (vertex: -1 compare to original graph)

def dijkstra(g): # O(n^2+m)
    n = len(g)
    d,p,u = [0]+(n-1)*[float('inf')], n*[None], n*[False]
    for i in range(n):
        v=-1
        for j in range(n):
            if not u[j] and (v==-1 or d[j]<d[v]):
                v=j
        if d[v]==float('inf'):
            break
        u[v]=True

        for k in range(len(g[v])):
            (to, length)=g[v][k]
            if d[v]+length<d[to]:
                d[to]=d[v]+length
                p[to]=v

    res=[]
    for m in range(n):
      path,v=[],m
      while v is not None:
          path.append(v)
          v=p[v]
      reversed(path)
      res.append((d[m],path))
    return res

assert dijkstra(g) == [(0, [0]), (7, [1, 0]), (9, [2, 0]), (20, [3, 2, 0]), (20, [4, 5, 2, 0]), (11, [5, 2, 0])]
