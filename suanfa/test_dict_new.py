# test_dict.py
# coding:utf-8
'''
'''
import collections
# combine two list, key_list, value_list
key_list = ['a','b','c','d']
value_list = [3,9,1,2]
dict1=dict(zip(key_list, value_list))
print sorted(dict1.items(),key=lambda dict1:dict1[1], reverse=False)
print sorted(dict1.items(),key=lambda dict1:dict1[1], reverse=True)
D5 = dict.fromkeys(key_list,0)
print D5
new_list = ['a','e','b','f','d'] # combile new_list to D5
for item in new_list:
	if item in D5.keys():
		D5[item]+=1
	else:
		D5[item]=0
print '==============>After=====>'
print D5


print '=========Scan the keys way1========='
for item in D5.keys():
	print item, '===>', D5[item]

print '==========Scan the keys way2====='
for key, value in D5.items():
	print key, '====>', value


'''
D5.keys()
D5.values()
D5.items()
'''