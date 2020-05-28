# coding: utf-8
'''
python有一些魔术方法，
1）__str__, __repr__

下面重写了__str__方法和__repr__方法。
其中：当print调用类的实例时，使用__str__方法
当交互式调用类的实例时，使用__repr__方法

2）__getattr__方法：获取类的属性。如果没有会报错
ClassA instance has no attribute 'a'
如果重写该函数，可以修改报错的方式

3）__new__方法：对于这些不可变的对象，我们只有通过__new__方法处理，才能得到我们想要的结果。
__new__ 和 __init_ 相配合,才是真正的类构造器。
其中之前有个例子就是用__new__来实现单例
'''
class ClassA():
    def __str__(self):
        return 'this is ClassA'
    def __repr__(self):
        return 'I am still ClassA'
    def __init__(self,plant,animal):
        self.plant=plant
        self.animal=animal
    def __getattr__(self, item):
        return 'no '+str(item)



if __name__ == '__main__':
    a = ClassA('Grass','Dog')
    print a.plant, a.animal, a.help