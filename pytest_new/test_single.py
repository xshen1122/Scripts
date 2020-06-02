# coding: utf-8
# class MusicPlayer(object):
#     def __new__(cls,*args, **kwargs):
#         return super.__new__(cls)
#
#
#     def __new__(cls):
#         print ("初始化音乐播放对象")
#
# player = MusicPlayer()
# print (player)
import time
class ClassA(object):
    #标志变量，保存第一个对象的引用
    instance = None
    flag = False
    def __new__(cls,*args, **kwargs):
        if cls.instance is None:
            cls.instance=super(ClassA).__new__(cls) #super不被python2.7支持
        return cls.instance
    def __init__(self):
        if not ClassA.flag:
            print ("init执行了")
            ClassA.flag=True
    # def __init__(self):
    #     print ("init执行了")

test1 = ClassA()
print (test1)
test2 = ClassA()
print (test2)

#循环和递归
#循环 - 线性，重复执行


#递归 - 非线性， 函数包含了对自身的调用
#可以解决循环的问题，要明确递归的终止条件


