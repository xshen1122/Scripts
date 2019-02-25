# test_class.py
# coding: utf-8
'''
# protected类型的变量和方法 在类的实例中可以获取和调用
# 私有类型的变量和方法 在类的实例中获取和调用不到
'''
class Student():
	def __init__(self,name='',age=0,gender='man'):
		self.__name = name
		self.age = age
		self.gender=gender
	def get_name(self):
		return self.__name
	def get_age(self):
		return self.age
	def get_gender(self):
		return self.gender
	def put_name(self,name):
		self.__name=name
	def __func(self):
		print 'This is a private method'
	def _func(self):
		print 'This is a protected method'

if __name__ == '__main__':
	s1 = Student('Tom',12,'man')
	print s1.get_name(),s1.get_age(), s1.get_gender()
	s2 = Student()
	print s2.get_name(),s2.get_age(), s2.get_gender()
	s2.put_name('Selina')
	print s2.get_name()
	s2._func()

