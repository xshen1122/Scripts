#coding: utf-8
import threading
import time

# 初始化两个锁
mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThread1(threading.Thread):
   def run(self):
       # 对mutexA上锁
       mutexA.acquire()

       # mutexA上锁后，延时1秒，等待另外一个线程。此时把mutexB上锁
       print(self.name + '-------do1-------up-------')
       time.sleep(1)

       # 此时会堵塞，因为这个mutexB已经被另外一个线程优先上锁了
       mutexB.acquire()
       print(self.name + '-------do1-------down-----')
       mutexB.release()

       # 对mutexA解锁，此时mutexB已经被堵塞，无法执行到这里的，那么就会锁住
       mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
       # 对mutexB上锁
       mutexB.acquire()

       # mutexB上锁后，延时1秒，等待另外一个线程。此时把mutexA上锁
       print(self.name + '-------do2-------up-------')
       time.sleep(1)

       # 此时会堵塞，因为这个mutexA已经被另外一个线程优先上锁了
       mutexA.acquire()
       print(self.name + '-------do-------down-----')
       mutexA.release()

       # 对mutexB解锁，此时mutexA已经被堵塞，无法执行到这里的，那么就会锁住
       mutexB.release()

def main():
    t1 = MyThread1()
    t2 = MyThread2()

    # 开启两个线程，此时两个线程会相互堵塞
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()