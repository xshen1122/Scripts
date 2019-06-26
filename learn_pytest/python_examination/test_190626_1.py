# test_190626_1.py
# coding: utf-8
'''
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

'''
from collections import deque
def find_num(yourlist):
	zheng_num=0
	fu_num=0
	for item in yourlist:
		if '-' in str(item):
			fu_num +=1
		else:
			zheng_num +=1



	return (zheng_num,fu_num)
'''
字符串 “axbyczdj”，如果得到结果“abcd”

'''

'''

已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
'''
'''
已知一个数字为1，如何输出“0001”
'''
'''
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
'''

'''
已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9

问题描述：用十进制计算30的阶乘，然后把结果转换成三进制表示，那么该进制表示的结果末尾会有多少个连续0？

012
作为笔试题的话，要想按照题意先把阶乘结果计算出来再转换成三进制最后再数0的个数，
时间肯定来不及。也就是说，应该是有更简单的方法。
以我们最熟悉的十进制为例，一个数乘以10相当于左移1位而右边补0；
了解二进制计算的朋友们应该知道，对一个二进制数乘以2相当于左移1位而右边补0。
恭喜，这对于任意素数进制都是成立的。也就是说，把从1到30的整数简单因数分解一下，
看看有多少个3，那么题目中最终计算结果末尾就有多少个0。

'''
def how_many_three():
	def number(num):
		if num%27==0:
			return 3
		elif num%9==0:
			return 2
		elif num%3==0:
			return 1
		else:
			return 0
	size=0
	for i in range(1,31):
		
		size += number(i)
	return size



if __name__ == '__main__':
	test_list = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
	print find_num(test_list)
	test_str = 'axbyczdj'
	print test_str[::2]
	test_str1= 'hello_world_yoyo'
	print test_str1.split('_')
	a=1
	print("%04d" % a)

	deque1 = deque([1,3,5,7])
	print deque1
	tmp1 = deque1[0]
	deque1.popleft()
	tmp = deque1[-1]
	deque1.pop()
	deque1.append(tmp1)
	deque1.append(tmp)
	print deque1

	print how_many_three()