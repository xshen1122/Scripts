# test_zhuangshiqi.py
# coding: utf-8
'''


'''
def use_logging_change(func):
	def wrapper(*args, **kwargs):
		print 'new added, logging print'
		return func(*args, **kwargs)
	return wrapper


@use_logging_change
def foo():
	print 'i am foo'
	# print 'new added, logging print' 
def use_logging(func):
	
	func()
	print 'new added, logging print'
@use_logging_change
def bar():
	print 'i am bar'

# use_logging(foo)
# use_logging(bar)



foo()
bar()

'''
as same as 
use_logging_change(foo)
foo()
'''

