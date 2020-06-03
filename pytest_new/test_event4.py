# coding: utf-8
# coding:utf-8

import threading
import time
import random

'''
主线程 -- ab多人 
event - 通知吃火锅
新加了一个end_event - 由吃火锅线程发送可以收拾的事件。
shoushi 进程start后一直在等待，等到了end_event被set后，就开始收拾。然后复位end_event
可以让别人用。
'''
def shoushi(guest):
    print '服务员正在等待收拾'
    count=0
    while count<guest:

        end_event.wait()
        print '吃完了，可以收拾了',threading.currentThread().getName()
        count +=1
        end_event.clear()

def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print '%s 已经启动' % threading.currentThread().getName()
    print '小伙伴 %s 已经进入就餐状态！' % name
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print '%s 收到通知了.' % threading.currentThread().getName()
    print '小伙伴 %s 开始吃咯！' % name
    time.sleep(5+random.randint(1,5))
    print '小伙伴 %s 吃完了！' % name
    end_event.set()


event = threading.Event()
end_event = threading.Event()

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a",))
thread2 = threading.Thread(target=chihuoguo, args=("b",))
thread3 = threading.Thread(target=shoushi,args=(2,))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)
# 发送事件通知
print '主线程通知小伙伴开吃咯！'
event.set()