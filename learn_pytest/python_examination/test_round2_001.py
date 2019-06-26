# test_round2_001.py
# coding: utf-8
class A(object):
    def show(self):
        print 'base show'

class B(A):
    def show(self):
        print 'derived show'

obj = B()
obj.show()