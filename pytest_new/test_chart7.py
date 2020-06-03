# coding: utf-8
from math import pi
from functools import total_ordering
from abc import ABCMeta, abstractmethod
import weakref



@total_ordering
class Shape(object):
    @abstractmethod
    def area(self):
        pass
    def __lt__(self,obj):
        print ' in __lt__'
        if not isinstance(obj,Shape):
            raise TypeError("not a shape class")
        return self.area() < obj.area()
    def __eq__(self,obj):
        print 'in __eq__'
        return self.area() == obj.area()
    def __gt__(self,obj):
        print 'in __gt__'
        return self.area() > obj.area()



class Rectangle(Shape):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h




class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self,value):
        if not isinstance(value,(int,float,long)):
            raise ValueError("bad value")
        else:
            self.radius = float(value)

    def area(self):
        return pi*self.radius**2

    R=property(getRadius,setRadius)

class Attr(object):
    def __init__(self,name,type_):
        self.name = name
        self.type_ = type_

    def __get__(self,instance, cls):
        print 'in __get__', instance, cls
        return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if not isinstance(value, self.type_):
            raise TypeError('expected type %s' % self.type_)
        print 'in __set__'
        instance.__dict__[self.name]=value

    def __delete__(self,instance):
        print 'in __delete__'
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name',str)
    age = Attr('age',int)
    height = Attr('height',float)

class Data(object):
    def __init__(self,value, owner):
        self.value=value
        self.owner=weakref.ref(owner)

    def __str__(self):
        return self.owner(), ':', self.value

    def __del__(self):
        print 'in Data.__del__'

class Node(object):
    def __init__(self,value):
        self.data = Data(value, self)
    def __del__(self):
        print 'in Node.__del__'


if __name__ == '__main__':
    node = Node(100)
    # import gc
    # gc.collect()
    del node
    raw_input('wait....')

    # p = Person()
    # p.name = 17
    # print p.name
    # a = A()
    # a.x=5
    # print a.x
    # c = Circle(3.2)
    # # c.radius = 'abc'
    # print c.R
    # c.R = 5.55
    # print c.R
    # r1 = Rectangle(5,1)
    # r2 = Rectangle(4,4)
    # c1 = Circle(1.0)
    # print r2 < c1
    # print c1>r1
