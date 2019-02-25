# test_bibao.py
# coding: utf-8
'''
out func and inner func

'''
def outer(a):
	b=10
	def inner():
		print (a+b)
	return inner
def new(a):
	b=10
	c=[a]
	def inner():
		
		print c[0]
		print b
	return inner

if __name__ == '__main__':
	# demo=outer(5)
	# demo()
	# print type(demo)
	demo = new(5)
	demo()
	print new(5).__closure__
	print outer(5).__closure__
	
