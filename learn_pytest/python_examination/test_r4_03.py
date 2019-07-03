# test_r4_03.py
# coding:utf-8
import math
import os
'''
通过dir可以获取模块的函数

'''
def test_math():
	for item in dir(math):
		print item
	print math.exp(4)
	print math.pow(4,4)
def test_os():
	print os.listdir('/home/real/SW')
	for root, dirs,files in os.walk('/home/real/SW'):
		print root, dirs, files


if __name__ == '__main__':
	test_os()