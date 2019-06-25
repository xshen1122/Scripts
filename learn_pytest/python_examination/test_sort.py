# test_sort.py
# coding:utf-8
student_tuples = [
('john', 'A', 15),
('jane', 'B', 12),
('dave', 'B', 10),
]

'''
说明：每一行的三个元素分别代表name, grade, age. 
请根据age分别对student_tuples及student_objects进行排序
'''

print sorted(student_tuples, key = lambda x: x[2])

class Student(object):
	def __init__(self,name,grade,age):
		self.name = name
		self.grade = grade
		self.age = age
	def __repr__(self):
		return repr((self.name, self.grade, self.age))

student_obj = [Student('john','A',15),
				Student('jane','B',12),
				Student('dave','B',10)]

print sorted(student_obj,key=lambda obj: obj.age)