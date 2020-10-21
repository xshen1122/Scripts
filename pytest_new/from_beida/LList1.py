# coding: utf-8
from LNode import LNode
from SingleLinkedList import LList
'''
以下为增加了尾节点的单链表
1. 增加尾节点的好处：
如果频繁的在尾部添加删除，可以减少复杂度，这样在表尾添加也可以做到O(1)
2. 思考， 新设计的链表和单链表非常相似，可以利用继承。不需要重写。
3. 写法： LList1(LList), 注意，如果括弧里不写，则继承object
'''

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self.rear = None  #尾节点，继承LList，增加尾节点，直接使用父类的__init__方法。

    def prepend(self, elem):#每一个操作要考虑head和rear的变化。比如在表头增加一个元素，表头肯定变化了，表尾出现2个情况，如果是往空表里增加，表尾就不是None，如果不是空表，表尾不变
        self.head = LNode(elem, self.head)
        if self.rear is None:  # empty list
            self.rear = self.head

    def append(self, elem):#往表尾增加。
        if self.rear is None:  # empty list
            self.prepend(elem)
        else:
            self.rear.next = LNode(elem, None)
            self.rear = self.rear.next

    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        if self.rear is self.head:  # list with one node
            self.rear = None
        self.head = self.head.next
        return e

    def poplast(self):
        return None  # to be implemented


if __name__ == '__main__':
    mlist1 = LList1()
    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()

