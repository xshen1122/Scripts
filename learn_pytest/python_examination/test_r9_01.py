# test_r9_01.py
# coding: utf-8
'''
How to use mmap

'''
from mmap import mmap

def get_lines(fp):
	with open(fp,'r+') as f:
		m=mmap(f.fileno(),0)
		for i,char in enumerate(m):
			print i,char
if __name__ == '__main__':
	fp = '/home/real/Videos/Log/auto_lossy/5.log'
	get_lines(fp)