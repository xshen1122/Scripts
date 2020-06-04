# coding: utf-8
import Queue, threading, time, random
'''
定义一个多线程类consumer， 功能是从队列中取数据，每次取一个
定义一个队列，里面放了10个数据
启动3个consumer，让他们从队列中取数，直到队列为空。（队列是线程安全的，其他数据类型不是）
'''

class consumer(threading.Thread): #消费者类
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.daemon = False
        self.queue = que

    def run(self):
        while True:
            if self.queue.empty(): #当队列为空，退出。
                break
            item = self.queue.get() #Remove and return an item from the queue
            # processing the item
            time.sleep(item)
            print self.name, item
            self.queue.task_done() #Indicate that a formerly enqueued task is complete

        return


que = Queue.Queue()
for x in range(10):
    que.put(random.random() * 10, True, None) #队列中有10个元素
consumers = [consumer(que) for x in range(3)] #由三个消费者从队列中取数，直到队列为空。

for c in consumers:
    c.start()
que.join() #Blocks until all items in the Queue have been gotten and processed

print '没有join就在开头或者中间执行这个打印'