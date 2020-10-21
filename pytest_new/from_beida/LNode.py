# coding: utf-8
class LNode :
    def __init__(self, elm, nxt=None):#这里有两种写法，一个是(self,elm,nxt), 一个是(self,elm,nxt=None).默认是None
        self.elem = elm
        self.next = nxt

if __name__ == '__main__':
    llist1 = LNode(1, None) #创建第一个节点
    pnode = llist1 #指针指向第一个节点

    for i in range(2, 11):
        s=LNode(i) #用一个变量存储新建的节点。
        pnode.next = s #将pnode的下一个节点指向新节点。
        pnode = s # 重置pnode，指向新节点。

    pnode = llist1
    while pnode != None:  #遍历各个节点
        print(pnode.elem)
        pnode = pnode.next #换到下一个节点
