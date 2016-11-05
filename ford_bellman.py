from collections import namedtuple

edge = namedtuple('edge', 'a b cost')

def ford_bellman_1(n,m,v,e):
    d=n*[float('inf')]
    d[v]=0

    for i in range(n-1):
        for j in range(m):
            if d[e[j].a]<float('inf'):
                d[e[j].b]=min(d[e[j].b],d[e[j].a]+e[j].cost)

    return d

def ford_bellman_2(n,m,v,e):
    d=n*[float('inf')]
    d[v]=0

    while True:
        any=False
        for j in range(m):
            if d[e[j].a]<float('inf'):
                if d[e[j].b]>d[e[j].a]+e[j].cost:
                    d[e[j].b]=d[e[j].a]+e[j].cost
                    any=True
        if not any:
            break

    return d

def ford_bellman_3(n,m,v,t,e):
    d=n*[float('inf')]
    d[v]=0
    p=n*[-1]

    while True:
        any=False
        for j in range(m):
            if d[e[j].a]<float('inf'):
                if d[e[j].b]>d[e[j].a]+e[j].cost:
                    d[e[j].b]=d[e[j].a]+e[j].cost
                    p[e[j].b]=e[j].a
                    any=True
        if not any:
            break

    if d[t]==float('inf'):
        raise Exception('No path: {}->{}'.format(v,t))

    path=[]
    cur=t
    while cur!=-1:
        path.append(cur)
        cur=p[cur]
    path.reverse()

    return path


def ford_bellman_4(n,m,v,e):
    d=n*[float('inf')]
    p=n*[-1]
    d[v]=0

    x=None
    
    for i in range(n):
        x=-1
        for j in range(m):
            if d[e[j].a]<float('inf'):
                d[e[j].b]=min(d[e[j].b],d[e[j].a]+e[j].cost)
                p[e[j].b]=e[j].a
                x=e[j].b

    if x==-1:
        raise Exception('No negative cycle from ',v)
    y=x
    path=[]

    cur=y
    while True:
        path.append(cur)
        if cur == y and len(path)>1:
            break
        cur=p[cur]
    path.reverse()
    return path

# https://upload.wikimedia.org/wikipedia/commons/d/de/Dijkstra_graph0.PNG
e=[
    edge(0,1,7),
    edge(0,2,9),
    edge(0,5,14),
    edge(1,2,10),
    edge(2,1,10),
    edge(1,3,15),
    edge(3,1,15),
    edge(2,5,2),
    edge(5,2,2),
    edge(2,3,11),
    edge(3,2,11),
    edge(3,4,6),
    edge(4,3,6),
    edge(4,5,9),
    edge(5,4,9)
]

assert ford_bellman_1(6,15,0,e)==ford_bellman_2(6,15,0,e)==[0, 7, 9, 20, 20, 11]
assert ford_bellman_3(6,15,0,4,e)==[0,2,5,4]
assert ford_bellman_3(6,15,0,5,e)==[0,2,5]

e2=[
    edge(0,1,7),
    edge(0,2,9),
    edge(0,5,14),
    edge(1,2,10),
    edge(2,1,10),
    edge(1,3,15),
    edge(3,1,15),
    edge(2,5,2),
    edge(5,2,2),
    edge(2,3,11),
    edge(3,2,11),
    edge(3,4,6),
    edge(3,5,-42),
    edge(5,3,-42),
    edge(4,3,6),
    edge(4,5,9),
    edge(5,4,9)
]

assert ford_bellman_4(6,17,0,e2)==[4,5,4]
