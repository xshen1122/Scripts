# test_subclass.py
# coding:utf-8
'''

'''

class Person(object):
    def __init__(self,name,sex):
    	self.name=name
    	self.sex=sex
    def print_title(self):
    	if self.sex=='male':
    		print 'man'
    	elif self.sex=='female':
    		print 'woman'

class Child(Person):  
	def __init__(self,name,sex,mother,father):	              # Child 继承 Person
		Person.__init__(self,name,sex)
		self.mother=mother
		self.father=father
	# def print_title(self):  # IndentationError: expected an indented block
 #    	if self.sex=='male':
 #    		print 'boy'
 #    	elif self.sex=='female':
 #    		print 'girl'



if __name__ == '__main__':
	May = Child('May','female','Lisa','Tom')
	Peter = Person('Peter','male') 
	# print(isinstance(May,Child))         # True
	# print(isinstance(May,Person))        # True
	# print(isinstance(Peter,Child))       # False
	# print(isinstance(Peter,Person))      # True
	# print(issubclass(Child,Person))
	May.print_title()
	print May.mother, May.father
	Peter.print_title()