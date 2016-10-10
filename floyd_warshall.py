i = float('inf')
g = [ [0,7,9,i,i,14],
      [7,0,10,15,i,i],
      [9,10,0,11,i,2],
      [i,15,11,0,6,i],
      [i,i,i,6,0,9],
      [14,i,2,i,9,0]
    ]
p = [[None for _ in range(6)] for _ in range(6)]

def floyd_warshall(d): # O(n^3)
    n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dk = d[i][k]+d[k][j]
                if dk<d[i][j]:
                    d[i][j]=dk
                    p[i][j]=k
    return g

def path(u,v):
    def path(u,v,paths):
        intermediate=p[u][v]
        if not intermediate:
            paths.append(u)
            return paths
        else:
            path(u,intermediate,paths)
            path(intermediate,v,paths)
        return paths
    return path(u,v,[])

assert floyd_warshall(g) == [[0, 7, 9, 20, 20, 11], [7, 0, 10, 15, 21, 12], [9, 10, 0, 11, 11, 2], [20, 15, 11, 0, 6, 13], [20, 21, 11, 6, 0, 9], [11, 12, 2, 13, 9, 0]]
assert path(0,4) == [0,2,5]
