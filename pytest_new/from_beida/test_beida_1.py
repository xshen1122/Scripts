# coding: utf-8
class Node(object):
    def __init__(self,value, next):
        self.value = value
        self.next = next
# 先定义一个类，Node，里面可以放value，和next 指向下一个node
if __name__ == '__main__':
    node1 = Node(1, None)
    head = node1
    for i in range(2, 10):
        new_node = Node(i, None) #先创建一个新的node
        head.next = new_node # 将head的下一个指向新的node
        head = new_node #将head挪到新的node上,不需要这一步。

    #遍历所有的node
    cursor = node1
    while cursor != None:
        print cursor.value
        cursor = cursor.next
