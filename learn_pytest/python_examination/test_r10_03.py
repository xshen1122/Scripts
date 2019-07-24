# test_r10_03.py
# coding: utf-8
import threading
import time
number = 0
def lock1():
	
	 
	def run(num):
	    global number
	    number += 1
	    print number
	    time.sleep(1)
	     
	for i in range(20):
	    t = threading.Thread(target=run, args=(i,))
	    t.start()


def lock2():
 
	
	 
	lock = threading.RLock()    #调用threading模块中的RLock()
	 
	def run(num):
	    lock.acquire()      #开始给线程加锁
	    global number
	    number += 1
	    lock.release()      #给线程解锁
	    print number
	    time.sleep(1)
	 
	for i in range(20):
	    t = threading.Thread(target=run, args=(i,))
	    t.start()

if __name__ == '__main__':
	lock1()
	time.sleep(10)
	lock2()