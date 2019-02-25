# test_q.py
# coding: utf-8
'''

How to use Queue
'''

import Queue
q=Queue.Queue(maxsize=2)
q.put('A') # put something into q
q.put('B')
print q.get() # get something out of q
print q.get()
if q.empty(): # judge if it's empty
	print 'Nothing can get'
print q.qsize()
print q.maxsize