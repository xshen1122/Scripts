# coding: utf-8
'''
练习一个二层装饰器
一个三层装饰器
主要用途：是不改变被修饰的函数的情况下，为函数添加其他功能
'''
def log(func):
    def wrapper(*args, **kwargs):
        print '这是一个二层装饰器,用来装饰其他函数'
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print "这是被装饰的函数"

def log_3(text):
    def decorate(func):
        def wrapper(*args,**kwargs):
            print text
            print "这是一个三层装饰器"
            return func(*args,**kwargs)
        return wrapper
    return decorate

@log_3("这是第三层装饰器的参数")
def now_3():
    print "这是一个被装饰的函数"
if __name__ == '__main__':
    now_3()