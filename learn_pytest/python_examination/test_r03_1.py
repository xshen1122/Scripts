# test_r03_1.py
# coding:utf-8
'''
find 100 - 200 all zhishu , output  10 numbers per line
主要难点是在于每10个数字输出一行，如何进行切片。

No2:
给定的二维数组中是否有重复的数。
已知该数组中保存了正整数
没有重复，返回真。不大于O(n)
将二维数组转换为1维数组，然后用set()
'''

def print_num():
	def check_zhishu(num):
		for i in range(2,num):
			if num%i ==0:
				return False
		return True
	zhishu_list = []
	for item in range(100,200):
		if check_zhishu(item):
			zhishu_list.append(item)
	print len(zhishu_list)
	for i in range(0,len(zhishu_list)/10):
		
		print zhishu_list [i*10:i*10+10]
		
	print zhishu_list[i*10+10:len(zhishu_list)]

def check_dup(D2_list):
	l1_tmp = D2_list[0]
	l2_tmp = D2_list[1]
	if len(set(l1_tmp + l2_tmp))< len(l1_tmp+l2_tmp):
		return False
	else:
		return True

if __name__ == '__main__':
	# print_num()
	dd=[[1,2],
	    [3,3],
	    [5,6]]
	print check_dup(dd)