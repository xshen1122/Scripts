# test_address.py
# coding: utf-8
'''
address
'''
def add_num(a,b):
	return a+b

if __name__ == '__main__':
	x=add_num
	y=add_num
	print type(x),type(y)
	print id(x), id(y), id(add_num) # too obvious, three of them are the same address.
	print x(3,4)