# coding: utf-8

def func1():
    try:
        open('1.txt','r')
    except (IOError,ZeroDivisionError), e :
        print e
    print 'this line is always printed'

def func2():
    open('1.txt','r')

def func3():
    input_value = 'abc'
    if not (input_value.isdigit()):
        raise ValueError('should be digit')  #手工抛出异常

if __name__ == '__main__':
    func1()