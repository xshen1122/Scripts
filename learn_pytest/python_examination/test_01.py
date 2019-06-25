# test_01.py
# coding: utf-8

def print_para(a,b,c=100, *args, **kw):
	print 'a=',a, ' b=',b, ' c=',c, ' args=',args, ' kw=', kw

class ClassTest(object):
	def __init__(self,a):
		self.a = a
	def printk(self):
		print 'a is ', self.a
	@classmethod
	def class_method(cls,*args):
		print 'args is ', args, type(args)
	@classmethod
	def class_method2(cls): #必须有cls参数     #这里第一个参数是cls， 表示调用当前的类名
		print 'cls is', cls, type(cls)
	@staticmethod
	def static_method(*args):
		print 'args is ', args,type(args)
def test_iter():
	l1 = [1,2,3,4]
	l2 = l1.__iter__()
	print l2
	print l2.next()


if __name__ == '__main__':
	# print_para(100,200,300,400,500,aa=500,bb=600,cc=700)
	# ct = ClassTest(100)
	# ct.printk()
	# ct.class_method()
	# ct.class_method2()
	# ct.static_method()

	# print '================'
	# ClassTest.class_method()
	# ClassTest.class_method2()
	# ClassTest.static_method()
	test_iter()

