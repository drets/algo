g = {
    1: [2,7,8],
    2: [3,6],
    3: [4,5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9,12],
    9: [10,11],
    10: [],
    11: [],
    12: []
} # https://upload.wikimedia.org/wikipedia/commons/1/1f/Depth-first-tree.svg

def dfs_rec(graph,start,path=[]):
    path.append(start)
    for edge in graph[start]:
        if edge not in path:
            dfs_rec(graph,edge,path)
    return path

def dfs(graph,start,path=[]):
    stack = [start]
    path = []
    while stack:
        v = stack.pop()
        path.append(v)
        for edge in reversed(graph[v]):
            if edge not in path:
                stack.append(edge)
    return path

assert dfs(g,1) == dfs_rec(g,1) == [1,2,3,4,5,6,7,8,9,10,11,12]
