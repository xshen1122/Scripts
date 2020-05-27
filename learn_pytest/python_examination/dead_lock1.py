#coding: utf-8
import threading
import time

lock_apple = threading.Lock()
lock_banana = threading.Lock()

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):

        lock_apple.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))

        lock_banana.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        lock_banana.release()
        lock_apple.release()


    def fun2(self):

        lock_banana.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        time.sleep(0.1)

        lock_apple.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))
        lock_apple.release()

        lock_banana.release()

if __name__ == "__main__":
    for i in range(0, 10):  #建立10个线程
        my_thread = MyThread()  #类继承法是python多线程的另外一种实现方式
        my_thread.start()

'''
1.fun1中，线程1先拿了苹果，然后拿了香蕉，然后释放香蕉和苹果，然后再在fun2中又拿了香蕉，sleep 0.1秒。

2.在线程1的执行过程中，线程2进入了，因为苹果被线程1释放了，线程2这时候获得了苹果，然后想拿香蕉

3.这时候就出现问题了，线程一拿完香蕉之后想拿苹果，返现苹果被线程2拿到了，线程2拿到苹果执行，想拿香蕉，发现香蕉被线程1持有了

4.双向等待，出现死锁，代码执行不下去了




'''