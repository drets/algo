g = {
    1: [2,3,4],
    2: [5,6],
    3: [],
    4: [7,8],
    5: [9,10],
    6: [],
    7: [11,12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
} # https://upload.wikimedia.org/wikipedia/commons/3/33/Breadth-first-tree.svg

def bfs(graph,start,path=[]):
    queue = [start]
    path.append(start)
    while queue:
        v = queue.pop(0)
        for edge in graph[v]:
            if edge not in path:
                path.append(edge)
                queue.append(edge)
    return path

assert bfs(g,1) == [1,2,3,4,5,6,7,8,9,10,11,12]
