# test_r6_02.py
# coding:utf-8
'''
Question1:
给定一个字符串a, 将a中的大写字母 转换成小写，其它字符不变，并输出。

例如：a="aaaaaabbbDDDDD"

则输出：aaaaaabbbddddd

Question3:
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。

例如a="cagy", b=3, 

则输出 ：fdjb
'''

import pytest
import os

def test_01():
	a = 'aaaaaabbbDDDDD'
	b = 'aaaaaabbbddddd'
	assert a.lower() == b
def test_02():
	a = "OurWorldIsFullOfLOVE"
	b = 'love'
	def compare(a,b):
		if b.lower() in a.lower():
			return 'LOVE'
		else:
			return 'SINGLE'
	assert compare(a,b) == 'LOVE'

if __name__ == '__main__':
	cmd = 'pytest test_r6_02.py'
	os.system(cmd)