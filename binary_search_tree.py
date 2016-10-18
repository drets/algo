class Node:
    def __init__(self,key,value):
        self.left=None
        self.right=None
        self.key=key
        self.value=value

class BSTree:
    def __init__(self):
        self.root=None

    def containsKey(self,k):
        x=self.root
        while x:
            if k<x.key:
                x=x.left
            elif k>x.key:
                x=x.right
            else:
                return True
        return False

    def get(self,k):
        x=self.root
        while x:
            if k<x.key:
                x=x.left
            elif k>x.key:
                x=x.right
            else:
                return x.value
        return None

    def add(self,k,v):
        x=self.root
        y=None
        while x:
            if k==x.key:
                x.value=v
                return
            else:
                y=x
                if k<x.key:
                    x=x.left
                else:
                    x=x.right
        newNode=Node(k,v)
        if not y:
            self.root=newNode
        else:
            if k<y.key:
                y.left=newNode
            else:
                y.right=newNode

    def remove(self,k):
        x=self.root
        y=None
        while x:
            if k==x.key:
                break
            else:
                y=x
                if k<x.key:
                    x=x.left
                else:
                    x=x.right
        if not x:
            return
        if not x.right:
            if not y:
                self.root=x.left
            else:
                if x==y.left:
                    y.left=x.left
                else:
                    y.right=x.left
        else:
            leftMost=x.right
            y=None
            while leftMost.left:
                y=leftMost
                leftMost=leftMost.left
            if y:
                y.left=leftMost.right
            else:
                x.right=leftMost.right
            x.key=leftMost.key
            x.value=leftMost.value

tree=BSTree()

tree.add("b",2)
tree.add("a",1)
tree.add("c",3)

assert not tree.containsKey("f")
assert tree.containsKey("b")
assert tree.containsKey("a")
assert tree.containsKey("c")

tree.add("d",4)
assert tree.containsKey("d")
assert tree.get("d")==4
tree.remove("d")
assert not tree.containsKey("d")

tree.add("d",42)
assert tree.containsKey("d")
assert tree.get("d")==42
tree.remove("d")
assert not tree.containsKey("d")

tree.remove("b")
tree.remove("a")
tree.remove("c")

assert not tree.containsKey("b")
assert not tree.containsKey("a")
assert not tree.containsKey("c")
