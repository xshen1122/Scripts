# test_condition.py
# coding: utf-8
'''
Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，
可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

实现场景：当a同学王火锅里面添加鱼丸加满后（最多5个，加满后通知b去吃掉），
通知b同学去吃掉鱼丸（吃到0的时候通知a同学继续添加）


'''
import threading
import time

con = threading.Condition()

num = 0

# 生产者
class Producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while True:
            print "开始添加！！！"
            num += 1
            print "火锅里面鱼丸个数：%s" % str(num)
            time.sleep(1)
            if num >= 5:
                print "火锅里面里面鱼丸数量已经到达5个，无法添加了！"
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
                # 等待通知
                con.wait()
        # 释放锁
        con.release()

# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while True:
            print "开始吃啦！！！"
            num -= 1
            print "火锅里面剩余鱼丸数量：%s" %str(num)
            time.sleep(2)
            if num <= 0:
                print "锅底没货了，赶紧加鱼丸吧！"
                con.notify()  # 唤醒其它线程
                # 等待通知
                con.wait()
        con.release()

p = Producer()
c = Consumers()
p.start()
c.start()