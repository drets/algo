class Grid:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.walls=[]
        self.weights={}

    def cost(self,from_node,to_node):
        return self.weights.get(to_node,1)

    def neighbors(self,t):
        (x,y)=t
        res=[]
        for (k,m) in [(x,y+1),(x-1,y),(x+1,y),(x,y-1)]:
            if k<0 or m<0 or k>self.width or m>self.height:
                continue
            if (k,m) in self.walls:
                continue
            res.append((k,m))
        return res

def gen_tile(graph,t,style):
    r='•'
    if 'number' in style and t in style['number']:
        r='{}'.format(style['number'][t])
    if 'point_to' in style and style['point_to'].get(t):
        (x1,y1)=t
        (x2,y2)=style['point_to'][t]
        if x2==x1+1:
            r='\u21D0'
        if x2==x1-1:
            r='\u21D2'
        if y2==y1+1:
            r='\u21D1'
        if y2==y1-1:
            r='\u21D3'
    if 'start' in style and t==style['start']:
        r='S'
    if 'goal' in style and t==style['goal']:
        r='G'
    return r

def gen_grid(graph,**style):
    res=''
    for y in range(graph.height):
        res+='\n'
        for x in range(graph.width):
            tile=gen_tile(graph,(x,y),style)
            res+='{tile: <{width}}'.format(tile=tile,width=3)
    return res

class PriorityQueue:

    def __init__(self):
        self.elements=[]

    @staticmethod
    def swap(lst,l,r):
        lst[l],lst[r]=lst[r],lst[l]

    def empty(self):
        return len(self.elements)==0

    def put(self,item,priority):
        def heap_decrease_key(a,i,x):

            def parent(i):
                return (i-1)//2

            if x[0]>a[i][0]:
                raise Exception('New key is less than current')
            a[i]=x
            while i>0 and a[parent(i)][0]>a[i][0]:
                self.swap(a,i,parent(i))
                i=parent(i)

        def min_heap_insert(a,x):
            a.append((float('inf'),item))
            heap_decrease_key(a,len(a)-1,x)

        min_heap_insert(self.elements,(priority,item))

    def get(self):
        def min_heapify(a,i):
            def left(i):
                return 2*i+1

            def right(i):
                return 2*(i+1)

            l,r,n=left(i),right(i),len(a)
            if l<n and a[l][0]<a[i][0]:
                minimum=l
            else:
                minimum=i
            if r<n and a[r][0]<a[minimum][0]:
                minimum=r
            if minimum is not i:
                self.swap(a,i,minimum)
                min_heapify(a,minimum)

        def extract_min(a):
            if len(a)==0:
                raise Exception('Queue is empty')
            min_val=a[0][1]
            a.pop(0)
            min_heapify(a,0)
            return min_val

        return extract_min(self.elements)

def heuristic(a,b):
    (x1,y1)=a
    (x2,y2)=b
    return abs(x1-x2)+abs(y1-y2)

def a_star_search(graph,start,goal):
    p=PriorityQueue()
    p.put(start,0)
    came_from,cost_so_far={},{}
    came_from[start],cost_so_far[start]=None,0

    while not p.empty():
        current=p.get()

        if current==goal:
            break

        for node in graph.neighbors(current):
            new_cost=cost_so_far[current]+graph.cost(current,node)
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node]=new_cost
                priority=new_cost+heuristic(goal,node)
                p.put(node,priority)
                came_from[node]=current

    return came_from,cost_so_far

grid=Grid(7,7)
grid.walls=[(3,1),(3,2),(3,3),(3,4),(3,5)]
grid.weights={(3,6):9}
start,goal=(0,3),(6,3)

came_from,cost_so_far=a_star_search(grid,start,goal)

def remove_whitespaces(s):
    return "".join(s.split())

e='''
⇑  ⇑  ⇑  ⇒  ⇒  ⇒  ⇒
⇑  ⇑  ⇑  •  ⇓  ⇒  ⇓
⇑  ⇑  ⇑  •  ⇓  ⇒  ⇒
S  ⇒  ⇒  •  ⇓  ⇒  G
⇓  ⇓  ⇓  •  ⇓  ⇓  •
⇓  ⇓  ⇓  •  •  •  •
⇓  ⇓  ⇓  ⇒  •  •  •
'''
a=gen_grid(grid,point_to=came_from,start=start,goal=goal)

e=remove_whitespaces(e)
a=remove_whitespaces(a)

assert a==e

e='''
3  4  5  6  7  8  9
2  3  4  •  8  9  10
1  2  3  •  9  10 11
S  1  2  •  10 11 G
1  2  3  •  11 12 •
2  3  4  •  •  •  •
3  4  5  14 •  •  •
'''
a=gen_grid(grid,number=cost_so_far,start=start,goal=goal)

e=remove_whitespaces(e)
a=remove_whitespaces(a)

assert a==e
