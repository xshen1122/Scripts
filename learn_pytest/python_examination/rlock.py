# rlock.py
# coding: utf-8
import threading
import time

lock = threading.RLock()  #递归锁


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):

        lock.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        lock.release()
        lock.release()


    def fun2(self):

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        time.sleep(0.1)

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))
        lock.release()

        lock.release()

if __name__ == "__main__":
    for i in range(0, 10):  #建立10个线程
        my_thread = MyThread()  #类继承法是python多线程的另外一种实现方式
        my_thread.start()

'''
为了支持在同一线程中多次请求同一资源，python提供了"递归锁"：threading.RLock。
RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，
从而使得资源可以被多次acquire。直到一个线程所有的acquire都被release，其他的线程才能获得资源。

'''