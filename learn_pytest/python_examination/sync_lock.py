# sync_lock.py
#coding=utf-8
import threading
import time
'''
charactors:
1. only 1 global 
2. only 1 lock
3. before add, acquire lock,after add, release lock
'''
g_num = 0

# 创建一个互斥锁
# 默认是未上锁的状态
mutex = threading.Lock()

def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 上锁
        g_num += 1
        mutex.release() # 解锁 
    print("----in work1, g_num is %d---"%g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 上锁
        g_num += 1
        mutex.release() # 解锁
    print("----in work2, g_num is %d---"%g_num)

def main():
    print("---线程创建之前g_num is %d---"%g_num)

    # 创建两个线程，各自对g_num进行相加
    t1 = threading.Thread(target=work1, args=(10000000,))
    t1.start()

    t2 = threading.Thread(target=work2, args=(10000000,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)

if __name__ == "__main__":
    main()

'''
first time:
---线程创建之前g_num is 0---
----in work2, g_num is 19820884---
----in work1, g_num is 20000000---
2个线程对同一个全局变量操作之后的最终结果是:20000000

second time:
---线程创建之前g_num is 0---
----in work2, g_num is 19739028---
----in work1, g_num is 20000000---
2个线程对同一个全局变量操作之后的最终结果是:20000000

锁的好处：

确保了某段关键代码只能由一个线程从头到尾完整地执行
 锁的坏处：

阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
 由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁

Avoid dead lock
综上所述，银行家算法是从当前状态出发，逐个按安全序列检查各客户谁能完成其工作，
然后假定其完成工作且归还全部贷款，再进而检查下一个能完成工作的客户，......。
如果所有客户都能完成工作，则找到一个安全序列，银行家才是安全的
'''