# quick_learn_007.py
# coding: utf-8
'''
single linklist
'''
class Node():
	def __init__(self,value,next=0):
		self.value=value
		self.next=next
class ListLink():
	def __init__(self):
		self.head=0
	def add(self,item):
		q=Node(item)
		if self.head==0:
			self.head=q
		else:
			p=self.head
			while p.next!=0:
				p=p.next
			p.next = q
	def print_all(self):
		p=self.head
		while p.next !=0:
			print p.value
			p=p.next
		print p.value


if __name__ == '__main__':
	ll = ListLink()
	ll.add(1)
	ll.add(3)
	ll.add(5)
	ll.add(7)
	ll.print_all()
