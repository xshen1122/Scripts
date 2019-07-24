# test_r10_1.py
# coding: utf-8
'''
@
'''

def use_logging_changed(func):
	def wrapper(*args, **kwargs):
		print 'new added'
		return func(*args,**kwargs)
	return wrapper

@use_logging_changed # define here!
def foo():
	print 'I am fool'

foo()

# ===================

'''
close package
'''
def outer(i):
    j = 1
    def inner():
        x = i + j
        print(x)
    return inner

test = outer(15)
test()
outer(15)()