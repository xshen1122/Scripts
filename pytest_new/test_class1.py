# coding: utf-8
'''
例题from lixuefeng
'''

class Student():
    count = 0
    def __init__(self,name,score=0,gender='male'):
        self.__name=name
        self.__score=score
        self.__gender=gender
        Student.count+=1
    def get_grade(self):
        if self.__score>90:
            return 'A'
        if self.__score>=60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if score in range(0,100):
            self.__score = score
        else:
            raise ValueError('bad value')
    def set_gender(self,gender):
        if gender in ['male','female']:
            self.__gender = gender
        else:
            raise ValueError('bad value')
    def get_gender(self):
        return self.__gender

class Animal(object):
    def run(self):
        print 'Animal is running'


class Dog(Animal):
    def run(self):
        print 'Dog is running'

class Cat(Animal):
    def run(self):
        print 'Cat is running'
class Turtle(Animal):
    def run(self):
        print 'Turtle is running very slow'

def run_twice(animal):
    animal.run()
    animal.run()

class MyStudent(Student):
    good_student = True

if __name__ == '__main__':
    if Student.count != 0:
        print('测试失败!')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')

    # dog = Dog()
    # cat = Cat()
    # dog.run()
    # cat.run()
    # animal=Animal()
    # run_twice(animal)
    # run_twice(dog)
    # run_twice(cat)
    # turtle=Turtle()
    # run_twice(turtle)



    # Lisa = Student('Lisa',90)
    # Bob = Student('Bob',91)
    # Tom = Student('Tom',60)
    # Tom.__score = 98 #如果不是私有的，可以从类的外面进行修改。修改成私有变了，无法从外部修改
    # Tom.set_score(96)
    # print Student #__main__.Student
    # print Lisa #<__main__.Student instance at 0x7f64ccb70b90>
    # print Tom.get_name(), Tom.get_score(), Tom.get_grade()
    #
    # bart = Student('Bart', 'male')
    # if bart.get_gender() != 'male':
    #     print('测试失败!')
    # else:
    #     bart.set_gender('female')
    #     if bart.get_gender() != 'female':
    #         print('测试失败!')
    #     else:
    #         print('测试成功!')