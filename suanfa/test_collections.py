# test_collections.py
# coding: utf-8
'''
module - test_collections

1. OrderedDict
2. namedtuple
3. deque
4. defaultdict
5. Counter
'''
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point',['x','y']) # define a Point
p=Point(1,2)  
print p.x, p.y
print isinstance(p,Point)
print isinstance(p,tuple)

#e.g, define a circle
Circle = namedtuple('Circle',['x','y','r'])


q1 = deque(['a','b','c'])
q1.append('FF')  # deque(['a', 'b', 'c', 'FF'])
print q1
q1.appendleft('QQ') # deque(['QQ', 'a', 'b', 'c', 'FF'])
print q1
print isinstance(q1, deque)

key=['a','b','c']
value = [2,3,4]
od = OrderedDict(zip(key,value))
print od
for key, value in od.items():
	print key, '--->', value
new_list = ['c','d','a','f']
for item in new_list:
	if item in od.keys():
		od[item] += 1
	else:
		od[item] = 1
print od

ct = Counter()
print isinstance(ct, dict)
print issubclass(Counter,dict)
for item in 'programmer':
	ct[item]+=1
print ct   # wolequ, so wonderful...

book = 'hello, world, you need a bed to sleep, you need a shafa to rest.'
ct1 = Counter()
word_list = book.split(' ')
for item in word_list:
	ct1[item]+= 1
print ct1