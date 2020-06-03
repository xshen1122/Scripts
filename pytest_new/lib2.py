# coding: utf-8
class Triangle(object):
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def getArea(self):
        a,b,c = self.l1, self.l2, self.l3
        p =(a+b+c)/2
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        return area