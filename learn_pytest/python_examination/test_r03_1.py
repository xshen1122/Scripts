# test_r03_1.py
# coding:utf-8
'''
find 100 - 200 all zhishu , output  10 numbers per line
主要难点是在于每10个数字输出一行，如何进行切片。
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



if __name__ == '__main__':
	print_num()