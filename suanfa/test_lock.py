# coding:utf-8
'''
Test Lock

3 threads will chang global count 
'''
import threading
# create a Lock
# lock = threading.Lock()
# print lock
# print type(lock)
# print lock.locked()
# print lock.acquire()

# rlock = threading.RLock()
# print type(rlock)
# print rlock
'''
由于多线程共享进程的资源和地址空间，
因此，在对这些公共资源进行操作时，
为了防止这些公共资源出现异常的结果，
必须考虑线程的同步和互斥问题。

通过threading.Lock()，就能实现加锁。
这样每个thread对count进行改动期间，
就不会有其它的thread插入进来改动count

直观看到，加锁之前，会有Thread-1,2,3几乎同时修改count的情况，从打印来看，
三条语句在一行。
Thread-2 changed count 265Thread-3 changed count 266Thread-1 changed count 267
加锁之后，没有同时修改count的情况。从打印来看，每个thread都是一条语句

加锁方法：
1. 先定义一个lock，再 with lock
2. 还有另一种用法，是通过Lock的acquire()和release()函数来控制加锁和解锁，如下例，得到的结果和上例相同：
if lock.acquire():
	xxx
	lock.release()
3. Lock vs RLock
从原理上来说：在同一线程内，对RLock进行多次acquire()操作，程序不会阻塞。


'''
count = 0
lock=threading.Lock()
def print_time(threadName):
	global count
	c=0
	if lock.acquire():
		while c<100:
			c+=1
			count+=1
			print '%s changed count %d'%(threadName,count)
		lock.release()

if __name__ == '__main__':
		t1 = threading.Thread(target=print_time,args = ("Thread-1",))
		t2 = threading.Thread(target=print_time,args = ("Thread-2",))
		t3 = threading.Thread(target=print_time,args = ("Thread-3",))	
		t1.start()
		t2.start()
		t3.start()