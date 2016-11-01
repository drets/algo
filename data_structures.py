import collections
import math

# stack without using build-in list
node=collections.namedtuple("node",['data','el'])

class stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        self.top=node(data,self.top)

    def pop(self):
        if self.empty():
            raise Exception('underflow')
        val=self.top.data
        self.top=self.top.el
        return val

    def empty(self):
        return not self.top

s=stack()

s.push(1)
s.push(2)
s.push(3)

assert not s.empty()
assert s.pop() == 3
assert s.pop() == 2
assert s.pop() == 1
assert s.empty()

# queue using 2 stacks
class queue:
    def __init__(self):
        self.s1,self.s2=stack(),stack()

    def enqueue(self,data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.empty():
            if self.s1.empty():
                raise Exception('Queue is empty')
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

q=queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

assert q.dequeue()==1
assert q.dequeue()==2
assert q.dequeue()==3

# heap

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def swap(a,l,r):
    a[l],a[r]=a[r],a[l]

def max_heapify(a,i):
    l,r,n=left(i),right(i),len(a)
    if l<n and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<n and a[r]>a[largest]:
        largest=r
    if largest is not i:
        swap(a,i,largest)
        max_heapify(a,largest)

def build_max_heap(a):
    for i in range(len(a)/2-1,-1,-1):
        max_heapify(a,i)

a=[4,1,3,2,16,9,10,14,8,7]
build_max_heap(a)

assert a==[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

def heap_sort(a):
    b=list(a)
    build_max_heap(b)
    res=[]
    for i in range(len(b)-1,-1,-1):
        res.insert(0,b[0])
        b.pop(0)
        max_heapify(b,0)
    return res

b=[4,1,3,2,16,9,10,14,8,7]
assert heap_sort(b)==[1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

# priority queue using heap

# O(lg n)
def extract_max(a):
    if len(a)<1:
        raise Exception('Queue is empty')
    max_val=a[0]
    a.pop(0)
    max_heapify(a,0)
    return max_val

# O(lg n)
def heap_increase_key(a,i,key):
    if key<a[i]:
        raise Exception('New key is less than current')
    a[i]=key
    while i>0 and a[parent(i)]<a[i]:
        swap(a,i,parent(i))
        i=parent(i)

# O(lg n)
def max_heap_insert(a,key):
    a.append(float('-inf'))
    heap_increase_key(a,len(a)-1,key)

c=[4,1,3,2,16,9,10,14,8,7]
build_max_heap(c)

assert extract_max(c)==16
assert c==[14, 10, 8, 7, 9, 3, 2, 4, 1]

d=[4,1,3,2,16,9,10,14,8,7]
build_max_heap(d)
heap_increase_key(d,8,15)
assert d==[16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

max_heap_insert(d,100)
assert d==[100, 16, 10, 14, 15, 9, 3, 2, 8, 1, 7]

