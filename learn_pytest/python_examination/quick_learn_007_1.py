# quick_learn_007_1.py
# coding: utf-8
'''
repeat...
'''

class Node():
	def __init__(self,value,next=0):
		self.value=value
		self.next = next
class LinkList():
	def __init__(self):
		self.head=0
	def append(self,item):
		q = Node(item)
		if self.head==0:
			self.head=q
		else:
			p=self.head
			while p.next!=0:
				p=p.next
			p.next=q
	def is_empty(self):
		if self.head==0:
			return True
		else:
			return False
	def print_all(self):
		if self.is_empty():
			print 'the linklist is empty'
		else:
			p=self.head
			while p.next !=0:
				print p.value
				p=p.next
			print p.value
	def add(self,item1,item2):
		p=self.head
		q=Node(item2)
		previous=Node(item1)
		while p.next.value != previous.value:
			p=p.next
		p=p.next
		after=p.next
		# print 'p is',p.value
	
		p.next= q
		q.next = after
	def delete(self,item):
		p=self.head

		while p.next.value!=item:
			p=p.next
			
		
		after = p.next.next
	
		p.next=after
	def add_head(self,item):
		q=Node(item)
		p=self.head
		self.head=q
		q.next = p
	def reverse(self):
		p=self.head
		ll2=LinkList()
		while p.next!=0:
			ll2.add_head(p.value)
			p=p.next
		ll2.add_head(p.value)
		ll2.print_all()
	def clear(self):
		self.head=0

if __name__ == '__main__':
	ll=LinkList()
	ll.append(2)
	ll.append(4)
	ll.append(6)
	ll.append(8)
	ll.append(10)
	ll.append(12)
	ll.append(14)
	ll.add(4,5)
	ll.add(5,5.5)
	ll.add(6,7)
	ll.print_all()
	print '====================='
	ll.delete(5.5)
	ll.print_all()
	print '====================='
	ll.add_head(1)
	ll.print_all()
	print '====================='
	ll.reverse()
	print '==============='
	ll.clear()
	ll.print_all()
