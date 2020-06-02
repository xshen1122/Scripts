# coding: utf-8

#sample1: 改写__new__
class IntTuple(tuple):
    #下面的new要重点理解
    def __new__(cls, gene):
        g=(x for x in gene if isinstance(x,int) and x>0)
        return super(IntTuple,cls).__new__(cls,g)

    def __int__(self,gene):
        print self
        #before
        super(IntTuple,self).__init__(gene)
        #after

#sample2:利用__slot__减少属性值占用内存
class Player1(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level



class Player2(object):
    __slots__=['uid','name','stat','level']
    def __init__(self,uid, name, status=0, level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level


if __name__ == '__main__':
    t=IntTuple([1,-1,'abc',[3,4],7])
    print t