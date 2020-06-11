# coding: utf-8
'''
加了缓存后，很快就计算出来了
下面将缓存的思路通用化，不在函数里面改写
'''
# def fib(n,cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#     #cache
#     if n<=1:
#         return 1
#     cache[n] = fib(n-1,cache)+fib(n-2,cache)
#     return cache[n]
def memo(func):
    cache={}
    def wrapper(*args,**kwargs):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrapper

@memo
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

# print fib(50)
@memo
def climb(n,steps):
    count = 0
    if n==0:
        count =1
    elif n>0:
        for step in steps:
            count += climb(n-step,steps)
    return count

# print climb(10,(1,2,3))
from functools import wraps, update_wrapper,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
def my_dec(func):
    @wraps(func)#或者直接用wraps来替换
    def wrapper(*args,**kwargs):
        ''' wrapper function'''
        print 'in wrapper'
        func(*args,**kwargs)
    # update_wrapper(wrapper,func,( '__name__' , '__doc__' ),('__dict__',))
    # update_wrapper(wrapper,func) #使用默认参数，就是上面的name，doc，dict
    return wrapper

@my_dec
def example():
    '''example function'''
    print 'in example function'

# print example.__name__
# print example.__doc__
# print example.__dict__

def typeassert(*ty_args, **ty_kwargs):
    def dec(func):

        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapper
    return dec

import time, logging
def warn(timeout):
    timeout = [timeout]
    def dec(func):
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = func.__name__, used , timeout[0]
                logging.warn(msg)
            return res
        def setTimeout(k):
            # nonlocal timeout# 在python3中使用nonlocal，我用global代替不行。
            timeout[0] = k

        wrapper.setTimeout = setTimeout
        return wrapper
    return dec
from random import randint
@warn(1.5)
def test():
    print 'in test'
    while randint(0,1):
        time.sleep(1)

# for _ in range(30):
#     test()

test.setTimeout(1)

for _ in range(30):
    test()