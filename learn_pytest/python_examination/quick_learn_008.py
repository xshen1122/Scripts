# quick_learn_008.py
# coding: utf-8

'''

built-in sort function
'''
import random
list_old=[]
for i in range(10):
	list_old.append(random.randint(1,1000000))
print list_old
print sorted(list_old)
list_old.sort(reverse=False)
print 'after ================'
print list_old
print sorted(list_old,key=lambda x:len(str(x)))

