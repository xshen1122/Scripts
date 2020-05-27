# coding: utf-8
import time

#闭包： 函数内变量只在函数内部有效， 利用返回值返回内部函数
#闭包函数私有化变量，完成了数据的封装，类似于面向对象

#装饰器 - 语法糖@，不影响原有函数功能，可以添加新的功能
def func():
    a=1
    def func1(num):

        print ('this is func1')
        print (num+a)
    return func1

var = func()
print (type(var))
var(3)




def log_3(text):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print (text)
            return func(*args,**kwargs)
        return wrapper
    return decorate

@log_3('this is the 3rd floor decorate')
def now():
    print (time.ctime())


now()

def args_func(sex):
    def decorate(func):
        def wrapper(*args,**kwargs):
            if sex == 'man':
                print ("你不能生娃")
            if sex == 'woman':
                print ("你可以生娃")

            return func(*args, **kwargs)
        return wrapper
    return decorate

@args_func(sex='man')
def man():
    print ('好好上班')

@args_func(sex='woman')
def woman():
    print ('好好上班')

man()
woman()