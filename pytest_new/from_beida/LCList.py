# coding: utf-8
from LNode import LNode
'''
单向循环链表和单向链表的唯一差别是： 单向链表的最后一个节点指向None
单向循环链表的最后一个节点指向head
 单向循环链表：
在单向链表中，头指针是相当重要的，因为单向链表的操作都需要头指针，
所以如果头指针丢失或者破坏，那么整个链表都会遗失，并且浪费链表内存空间。

我在思考一个问题，单链表的话一般要建个头指针，这样操作起来方便，
单循环链表要一般建个尾指针，这样也可以找到头结点，
合并两个单循环链表也很容易，时间复杂度是O(1)，
'''

class LCList:  # class of Circular Linked List单向循环列表，并不是LList的子类
    def __init__(self):
        self.rear = None #没有head，只有一个rear

    def isEmpty(self):
        return self.rear is None #判断尾是否为空

    def prepend(self, elem):  # add element in the front end
        p = LNode(elem, None) #新建一个节点
        if self.rear is None: #如果是空表
            p.next = p  # initiates circle,表中第一个节点建立初始的循环链接
            self.rear = p
        else:
            p.next = self.rear.next #链接在尾节点之后，就是新的首节点
            self.rear.next = p

    def append(self, elem):  # add element in the rear end
        self.prepend(elem)
        self.rear = self.rear.next

    def pop(self):  # pop out head element
        if self.rear is None:
            raise ValueError
        p = self.rear.next
        if self.rear is p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.elem

    def printall(self):
        p = self.rear.next
        while True:
            print(p.elem)
            if p is self.rear:
                break
            p = p.next


if __name__ == '__main__':
    mlist = LCList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    # mlist.printall()
    print '---------'
    while not mlist.isEmpty():
        print(mlist.pop())

