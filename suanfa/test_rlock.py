# test_rlock.py
# coding: utf-8
'''
RLock
每个thread都运行f()，
f()获取锁后，运行g()，但g()中也需要获取同一个锁。
如果用Lock，这里多次获取锁，就发生了死锁
'''

import threading
lock = threading.RLock() # using RLock, no problem
# lock = threading.Lock() # cannot run the program

def f():
	with lock:
		g()
		h()

def g():
	with lock:
		h()
		do_something1()

def h():
	with lock:
		do_something2()

def do_something1():
	print 'do something1'

def do_something2():
	print 'do something2'

if __name__ == '__main__':
	t1 = threading.Thread(target=f,)
	t2 = threading.Thread(target=f,)
	t3 = threading.Thread(target=f,)

	t1.start()
	t2.start()
	t3.start()
