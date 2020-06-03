# coding: utf-8
from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle
from operator import methodcaller

def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            # print f
            return f()
            # return methodcaller(name)(shape)


shape1 = Circle(2)
shape2 = Triangle(3,4,5)
shape3= Rectangle(6,4)

shapes = [shape1, shape2, shape3]
print map(getArea,shapes)