# test_100_7.py
# coding:utf-8
'''
线性表的链式存储结构
在python中如何实现？
插入这块不会了。节点的定义
看了两个网上的实现都感觉不好，还得是伯乐啊
http://python.jobbole.com/83953/
增加和插入，删除不知道咋处理
add-在链表前端添加元素
在链表前端添加元素，较为简单，就是在head前面添加。注意每个链表初始化时，都有一个head
添加到head前面
1）建立一个tmp Node = Node（value)
2) tmp.next = self.head
3) self.head = tmp
append-在链表后端添加元素
这个比较复杂，先要判断是否为空，如果是空：
self.head = tmp(value)
如果不为空，必须遍历整个链表
current = self.head
while tmp.next !=None:
    current = current.next
current.next = tmp

'''
class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class NodeList(object):
	def __init__(self):
		self.head=None
		self.size=0
	def isEmpty(self):
		return self.head==None
	def add(self,value):
		temp=Node(value)
		temp.next=self.head
		self.head=temp
	
	def append(self,value):
		temp=Node(value)

		if self.isEmpty():
			self.head=temp
		else:
			current = self.head
			while current.next !=None:
				current = current.next
			current.next = temp

if __name__ == '__main__':
	nlist = NodeList()
	print nlist.append(5)
	print nlist.append(6)
	print nlist.append(7)





	

