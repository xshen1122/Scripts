# test_r3_05.py
# coding: utf-8
'''
3、编写程序，生成一个包含20个随机整数的列表，
然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变。（提示：使用切片。） 
取数组的偶数下标
list1[::2]
取数组的奇数下标
list1[1::2]
'''

import random
test_list = []
new_list = []
for i in range(20):
	test_list.append(random.randint(10,100))
print test_list
even_list = test_list[0::2]
new_list = sorted(even_list,reverse=True)
test_list[0::2]=new_list
print test_list
