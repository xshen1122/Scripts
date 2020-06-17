# coding: utf-8
from blinker import signal
'''
Blinker是一个基于Python的强大的信号库，支持一对一、一对多的订阅发布模式，
支持发送任意大小的数据等等，且线程安全。

pip install blinker

refer from: 
https://www.jianshu.com/p/829da3cd70b6

'''

# singleton
a = signal('signal_test')

b = signal('signal_test')

# print a is b

#订阅信号,使用.connect(func)方法来订阅一个信号，当信号发布时，该信号的订阅者会执行func。
def subscriber(sender):
    print 'got a signal from: {}'.format(sender)

ready = signal('ready')
ready.connect(subscriber)

#使用.send()方法来发布信号，会通知所有订阅者，如果没有订阅者则什么都不会发生
class Processor():
    def __init__(self,name):
        self.name = name

    def go(self):
        ready1 = signal('ready')
        ready1.send(self)
        print('Processing...')
        complete = signal('complete')
        complete.send(self)

    def __repr__(self):
        return 'Processor: ' + self.name

processor_a = Processor('a')
print processor_a
processor_a.go()




