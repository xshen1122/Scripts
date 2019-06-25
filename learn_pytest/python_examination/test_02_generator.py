# test_02_generator.py
# coding: utf-8
import time
def genrator_fun1():
    a = 1
    print('现在定义了a变量')
    yield a
    b = 2
    print('现在又定义了b变量')
    yield b

g1 = genrator_fun1()
print('g1 : ',g1)       #打印g1可以发现g1就是一个生成器
print('-'*20)   #我是华丽的分割线
print(next(g1))
time.sleep(5)   #sleep一秒看清执行过程
print(next(g1))

#初识生成器二

def produce():
    """生产衣服"""
    for i in range(2000000):
        yield "生产了第%s件衣服"%i

product_g = produce()
print(product_g.__next__()) #要一件衣服
print(product_g.__next__()) #再要一件衣服
print(product_g.__next__()) #再要一件衣服
num = 0
for i in product_g:         #要一批衣服，比如5件
    print(i)
    num +=1
    if num == 5:
        break

#到这里我们找工厂拿了8件衣服，我一共让我的生产函数(也就是produce生成器函数)生产2000000件衣服。
#剩下的还有很多衣服，我们可以一直拿，也可以放着等想拿的时候再拿

import time


def tail(filename):
    f = open(filename)
    f.seek(0, 2) #从文件末尾算起
    while True:
        line = f.readline()  # 读取文件中新的文本行
        if not line:
            time.sleep(0.1)
            continue
        yield line

tail_g = tail('tmp')
for line in tail_g:
    print(line)

