# coding: utf-8
'''
This is for __slot__


'''

class Student(object):
    __slots__=('sex','age')
    pass
class SubStudent(Student):
    pass
s = SubStudent()
s.name = 'bob'
print s.name #在这里是可以直接赋值s.name的，在类里面无须定义

#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

#Python内置的@property装饰器就是负责把一个方法变成属性调用的
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Screen(object):
    def width(self):
        return self._width
    def height(self):
        return self._height

    @property #通过property来定义只读属性
    def resolution(self):
        return self.width*self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

from enum import Enum

class Gender(Enum):
    Female=0
    Male=1

class Person():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

s = Person('Steven',Gender.Male)

print s.name, s.gender