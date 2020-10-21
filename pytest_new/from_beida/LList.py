# coding: utf-8
from LNode import LNode
'''
单向链表的应用
1. 反转 rev - 就是两个节点交换，正序是1指向2， 反序后就是2指向1， 全部搞定后，再将p设为头节点。
思考， 单从code上看不清楚逻辑关系，就要一步步打印调试，来看清楚到底是怎么做的。
2. 排序 sort
有两种方法， sort和sortm

'''

class LList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e

    def append(self, elem):
        if self.head is None:
            self.head = LNode(elem, None)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None)

    def poplast(self):
        if self.head is None:  # empty list
            raise ValueError
        p = self.head
        if p.next is None:  # list with only one element
            e = p.elem;
            self.head = None
            return e
        while p.next.next is not None:  # till p.next be last node
            p = p.next
        e = p.next.elem;
        p.next = None
        return e

    def find(self, pred):
        p = self.head
        while p is not None:
            if pred==(p.elem):
                return p.elem
            p = p.next
        return None

    def printall(self):
        p = self.head
        while p is not None:
            print p.elem
            # if p.next is not None:
            #     print', '
            p = p.next
        print('')

    def rev(self):
        p = LNode('null', None)
        while self.head is not None:
            q = self.head
            # print '1. 当前的头节点为:', q.elem
            self.head = q.next
            # print '2. self.head 往下挪了一个 ', self.head.elem
            q.next = p  # 节点1指向None，翻转为尾节点
            print '3.  ', q.elem, '节点指向', p.elem, '节点'
            p = q
            # print '4, p节点更新为： ', p.elem
            print ' ======'
        self.head = p

    def sortm(self): #移动元素，每次拿一个元素，在已排序的序列中找到合适位置插入
        if self.head is None:
            return
        crt = self.head.next
        # print '当前节点为', crt.elem,'此时head为', self.head.elem
        while crt is not None:
            x, p = crt.elem, self.head
            # print '将当前节点的值存下来', x, '将head存下来', p.elem
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
                # print 'p不是head，p有两个地方进行更新，head是最小值', self.head.elem,'相等吗？'
            crt.elem = x
            # print '当前节点为', crt.elem
            crt = crt.next
            # print '将当前节点往下挪一个', crt.next.elem
            print '-------'
            self.printall()
            print '-------'
        # print '当前head为：', self.head.elem

    def sort(self):
        if self.head is None:
            return
        last = self.head;
        crt = last.next
        while crt is not None:
            p = self.head;
            q = None
            while p is not crt and p.elem <= crt.elem:
                q = p;
                p = p.next
            if p is crt:
                last = crt
            else:
                last.next = crt.next
                crt.next = p
                if q is None:
                    self.head = crt
                else:
                    q.next = crt
            crt = last.next
            print '--------'
            self.printall()
            print '--------'
        # end of class LList


def listSort(lst): #插入排序法，先维护一段排好序的列表，当有新元素进来的时候，放到合适的位置上
    for i in range(1, len(lst)):  # seg [0:0] is sorted
        print 'this is, ', i, lst
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:  # moving one by one
            lst[j] = lst[j - 1]  # in reversed-order
            j -= 1
        lst[j] = x


import random

if __name__ == '__main__':
    # list1 = [random.randint(1, 50) for i in range(3)]
    # list1 = [32, 25, 13, 10, 7]
    # # print(list1, '\n')
    # listSort(list1)
    # print '最后结果', list1
    # print '利用sorted函数',sorted(list1)
    # list1.sort()
    # print '利用sort函数', list1

    mlist1 = LList()

    # for i in range(5):
    #     mlist1.prepend(i)
    mlist1.prepend(3)
    mlist1.prepend(14)
    mlist1.prepend(20)
    mlist1.prepend(8)
    mlist1.prepend(17)
    mlist1.printall()
    print '------'
    #
    # for i in range(11, 20):
    #     mlist1.append(i)

    # mlist1.printall()
    # for i in range(5):
    #     print(mlist1.pop())
    #     print(mlist1.poplast())

    # print('remained:')
    # mlist1.printall()
    # mlist1.rev()
    # print('\nreversed:')
    # mlist1.printall()

    mlist1.sort()
    print('\nsorted:')
    # mlist1.printall()



