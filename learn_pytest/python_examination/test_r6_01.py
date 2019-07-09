# test_r6_01.py
# coding:utf-8
'''
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

例如：a={1:1,2:2,3:3}, 则输出：1,2,3

给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".

Question2:
给你平面上两个点的坐标(x1, y1), (x2, y2)， 请你计算并输出它们之间的距离，结果保留到小数点后两位。

例如：x1=0, y1=0, x2=0, y2=1

   则输出：1.00

Question3
给你一个高为n (0 < n < 100)，宽为m(0 < m < 100)列的网格，计算出这个网格中有共多少个矩形，下图为高为2，宽为4的网格.
n = 1, m = 2时，输出：3

n = 2, m = 4时，输出：30

Question4
给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。

例如： L=[0,1,2,3,4]

则输出：2
'''
import pytest
import os
import math
def get_result(a):
	a_order_list = sorted(a.keys())
	return a_order_list
def test_01():
	a = {1:1,2:2,3:3}

	assert get_result(a) == ([1,2,3])


def get_distance(x1,y1,x2,y2):
	x1=float(x1)
	y1=float(y1)
	x2=float(x2)
	y2=float(y2)
	result = math.sqrt((x1-x2)**2+(y1-y2)**2)
	return round(result,2)
def test_02():
	x1=0
	y1=0
	x2=0
	y2=1
	assert get_distance(x1,y1,x2,y2) == 1.00


def get_rectangle(n,m):
	x=range(1,m+1)
	y=range(1,n+1)
	return sum(x)*sum(y)
def test_03():
	assert get_rectangle(1,2)==3
	assert get_rectangle(2,4)==30

def get_middle(list1):
	#assume list1 is ordered
	if len(list1)%2 == 1:
		middle_value = round(list1[len(list1)/2],1)
	else:
		middle_value = round((list1[len(list1)/2]+list1[len(list1)/2-1])/2,1)
	return middle_value
def test_04():
	list1 = [1,2,3,4,5]
	list2 = [2,4,5,7,9,11]
	assert get_middle(list1) == 3.0
	assert get_middle(list2) == 6.0

if __name__ == '__main__':
	cmd = 'pytest test_r6_01.py'
	os.system(cmd)
	