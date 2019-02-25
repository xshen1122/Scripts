# simulate producer/consumer model
#coding: utf-8
'''


'''
import threading, time, Queue
q = Queue.Queue() #create a Queue instance

def Produce(name):
	count=0
	while count<10:
		print 'cooker %s is making baozi'%name
		time.sleep(2)
		q.put(count)

		print 'produce%s has made the %s baozi'%(name,count)
		count +=1
		print 'ok....'
def Consumer(name):
	count =0
	while count<10:
		time.sleep(2)
		if not q.empty():
			data = q.get()
			print 'Consumer %s has eaten the %s baozi' %(name,data)
		else:
			print 'All baozi have been eaten out'
		count += 1
def Produce1(name):
	count = 0
	while count<10:
		print 'Cooker %s is making baozi'%name
		time.sleep(2)
		q.put(count)
		print 'produce %s has made the %s baozi'%(name,count)
		count+=1
		q.task_done()
		q.join()
		print 'ok.....'
def Consumer1(name):
	count=0
	while count<10:
		time.sleep(2)
		print 'waiting'
		q.join()
		data=q.get()
		print '%s is eating'%name
		time.sleep(4)
		q.task_done
		print'%s has eaten %s baozi'%(name,data)
		count+=1



if __name__ == '__main__':
	p1 = threading.Thread(target=Produce1,args = ('A1 cooker',))
	c1 = threading.Thread(target=Consumer1,args = ('B customer',))
	c2 = threading.Thread(target=Consumer1,args = ('C customer',))
	c3 = threading.Thread(target=Consumer1,args = ('D customer',))
	p1.start()
	
	c1.start()
	c2.start()
	c3.start()





