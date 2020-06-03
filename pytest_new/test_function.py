# coding: utf-8
'''
练习：过滤目录下文件内容包含error的文件

grep –rl ‘error’ /dir
使用os模块walk方法：

os.walk会把目录下的二级目录和文件做成一个迭代器，多次使用实现文件路径的拼接
1. 不能理解@init有设么用？

'''

import os

#先定义了一个装饰器，功能：取生成器的下一个元素
def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


# 第一阶段：找到所有文件的绝对路径
@init
def search(target):
    while True:
        filepath = yield
        g = os.walk(filepath)
        for pardir, _, files in g:
            for file in files:
                abspath = r'%s/%s' % (pardir, file)
                target.send(abspath) #用到了send方法


# 第二阶段：打开文件
@init
def opener(target):
    while True:
        abspath = yield
        with open(abspath, 'rb') as f:
            target.send((abspath, f))


# 第三阶段：循环读出每一行内容
@init
def cat(target):
    while True:
        abspath, f = yield  # (abspath,f)
        for line in f:
            res = target.send((abspath, line))
            if res: break


# 第四阶段：过滤
@init
def grep(pattern, target):
    tag = False
    while True:
        abspath, line = yield tag
        tag = False
        if pattern in line:
            target.send(abspath)
            tag = True


# 第五阶段：打印该行属于的文件名
@init
def printer():
    while True:
        abspath = yield
        print(abspath)

if __name__ == '__main__':

    g = search(opener(cat(grep('error'.encode('utf-8'), printer()))))
    g.send('/home/real/Script/pytest_new')