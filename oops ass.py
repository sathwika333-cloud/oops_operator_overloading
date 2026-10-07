class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(10)
b2=Book(20)
print(b1+b2)

class Employee:
    def __init__(self,sal):
        self.sal=sal
    def __gt__(self,other):
        return self.sal > other.sal
e1=Employee(50000)
e2=Employee(25000)
print(e1>e2)

class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def __mul__(self,other):
        return self.l*other.l*self.w*other.w
a1=Rectangle(5,4)
a2=Rectangle(3,2)
print(a1*a2)

class Temp:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        return self.value-other.value
v1=Temp(50)
v2=Temp(20)
print(v1-v2)

class Time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    def __add__(self,other):
        h=self.h+other.h
        m=self.m+other.m
        if m>60:
            h=h+1
            m=m-60
        return h,m
t1=Time(2,50)
t2=Time(3,60)
print(t1+t2)

class Shoppingcart:
    def __init__(self,prices):
        self.prices=prices
    def __add__(self,other):
        return self.prices+other.prices
p1=Shoppingcart([100,250,300])
p2=Shoppingcart([200,800])
print(p1+p2)

class Dist:
    def __init__(self,m):
        self.m=m
    def __add__(self,other):
        return self.m+other.m
    def __sub__(self,other):
        return self.m-other.m
    def __eq__(self,other):
        return self.m==other.m
m1=Dist(100)
m2=Dist(10)
print(m1+m2)
print(m1-m2)
print(m1==m2)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return (self.x+other.x) , (self.y+other.y)
    def __sub__(self,other):
        return (self.x-other.x) , (self.y-other.y)
    def __mul__(self,other):
        return (self.x*other.x) +(self.y*other.y)
v1=Vector(2,3)
v2=Vector(4,5)
print(v1+v2)
print(v1-v2)
print(v1*v2)
