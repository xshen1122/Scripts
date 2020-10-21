# coding: utf-8
from LNode import LNode #利用已经存在的LNode类。
'''
以下是单链表。只有一个head。没有尾节点。

'''

class LList: #定义单向链表
    def __init__(self):
        self.head = None #初始化链表，主要是head指向None

    def isEmpty(self):
        return self.head is None #判断链表是否为空，用head指向是否为None来判断。

    def prepend(self, elem):
        self.head = LNode(elem, self.head)#向表头插入一个元素，这个需要重点理解

    def pop(self):  #弹出链表的表头
        if self.head is None: #判断下链表是否为空，如果是空，抛出ValueError
            raise ValueError
        e = self.head.elem  #非空的话，保留表头
        self.head = self.head.next #将表头更新为下一个元素
        return e

    def append(self, elem): #向链表的末尾添加一个元素
        if self.head is None: #判断下，如果为空表，就直接添加。
            self.head = LNode(elem, None)
            return
        p = self.head #将指针从表头开始，一直循环操作到表末尾为止。
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None) #在末尾添加一个元素

    def poplast(self): # 弹出最后一个元素，分成3种情况，1）如果空表，2）如果只有一个元素-主要考虑head指向谁，3）如果有多个元素
        if self.head is None:  # empty list
            raise ValueError
        p = self.head
        if p.next is None:  # list with only one element
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:  # till p.next be last node
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred): #查找某个元素
        p = self.head
        while p is not None:
            if pred==(p.elem):# 遍历整个链表的节点
                return p.elem
            p = p.next
        return None

    def printall(self): #打印出所有单链表元素
        p = self.head
        while p is not None:#遍历链表
            print(p.elem)
            p = p.next


if __name__ == '__main__':
    mlist1 = LList()

    for i in range(100,102):
        mlist1.prepend(i)

    for i in range(300,303):
        mlist1.append(i)

    mlist1.printall()
    mlist1.pop()
    mlist1.printall()
    mlist1.poplast()
    mlist1.printall()




