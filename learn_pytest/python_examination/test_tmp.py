# test_tmp.py
# coding: utf-8
char = 'a'
print len(char)

d1 = {'1':1, '2':2}
dcopy = d1
d1['1']=5
print d1['1'] + dcopy['1']

g = 0
def add():
	global g
	print 'g=',g

	g=g+1
	return g

print add()
print add()
print add()


def check_str(yourstr):
	if isinstance(yourstr, str):
		print 'yes'
	else:
		print 'no'
check_str('abc')

t1 = (1,2,3)
print list(t1)
print tuple(list(t1))

l1 = [1,2,3]
l2 = [4,5,6]
print list(set(l1).intersection(set(l2)))
print list(set(l1).union(set(l2)))
print list(set(l1).difference(set(l2)))


dict1 = {'a':1, 'b':10, 'c':20}
def get_pair(dict1):
	list1 = []
	for item in dict1.keys():
		list1.append((item, dict1[item]))
	return list1

print get_pair(dict1)

def delete_dup(yourlist):
	yourlist = list(set(yourlist))
	return (yourlist)

test_list =[1,2,3,1,4]
print delete_dup(test_list) 

def log(func):
	def wrapper(*args, **kwargs):
		print 'call',func.__name__,'()'
		return func(*args, **kwargs)
	return wrapper

@log
def now():
	print '2017-08-31'
now()

def add_dict(d1,d2):
	key1_list = d1.keys()
	key2_list = d2.keys()
	print key1_list, '===', key2_list
	key_total_list = list(set(key1_list).union(set(key2_list)))
	total_dict={}
	print key_total_list
	# for item in key_total_list:
	# 	total_dict[item]=0
	
	for item in key_total_list:
		if item in key1_list and item not in key2_list:
			print 'level1',item
			total_dict[item] = d1[item]

		elif item in key2_list and item not in key1_list:
			print 'level2',item
			total_dict[item] = d2[item]
		elif item in key1_list and item in key2_list:
			print 'level3',item
			total_dict[item] = d1[item] + d2[item]
	return total_dict

d1 = {'a':1,'b':2, 'c':3, 'd':4, 'f':'hello'}
d2 = {'g':5,'a':6,'b':4,'d':15,'k':'world'}
print add_dict(d1,d2)

import json
'''
data:{'time':"2016-08-21",
      'some_id':'ABCD',
      'grp1':{'fid1':1, 'fid2':2}}


'''
data = '{"time":"2016-08-21","some_id":"ABCD","grp1":{"fid1":1, "fid2":2}}'
dict1 = json.loads(data)
print dict1['time']