class pt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def area(a,b,c):
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)

def intersect_1(a,b,c,d):
    if a>b:
        a,b=b,a
    if c>d:
        c,d=d,c
    return max(a,c)<=min(b,d)

def intersect(a,b,c,d):
    return intersect_1(a.x,b.x,c.x,d.x) and \
        intersect_1(a.y,b.y,c.y,d.y) and \
        area(a,b,c)*area(a,b,d)<=0 and \
        area(c,d,a)*area(c,d,b)<=0

a=pt(0,0)
b=pt(10,0)
c=pt(5,0)
d=pt(5,10)
assert intersect(a,b,c,d)
c=pt(5,1)
assert not intersect(a,b,c,d)

eps=0.000000001

def det(a,b,c,d):
    return a*d-b*c

def between(a,b,c):
    return min(a,b)<=c+eps and c<=max(a,b)+eps

def intersect_2(a,b,c,d):
    a1,b1=a.y-b.y,b.x-a.x
    c1=-a1*a.x-b1*a.y
    a2,b2=c.y-d.y,d.x-c.x
    c2=-a2*c.x-b2*c.y
    zn=det(a1,b1,a2,b2)
    if zn!=0:
        x=-det(c1,b1,c2,b2)*float(1)/zn
        y=-det(a1,c1,a2,c2)*float(1)/zn
        return between(a.x,b.x,x) and between(a.y,b.y,y) and \
            between(c.x,d.x,x) and between(c.y,d.y,y)
    else:
        return det(a1,c1,a2,c2)==0 and det(b1,c1,b2,c2)==0 and \
            intersect_2(a.x,b.x,c.x,d.x) and intersect_2(a.y,b.y,c.y,d.y)

a=pt(0,0)
b=pt(10,0)
c=pt(5,0)
d=pt(5,10)
assert intersect_2(a,b,c,d)
c=pt(5,1)
assert not intersect_2(a,b,c,d)
