# test_r8_02.py
# coding: utf-8
'''
经典的猜数字游戏，几乎所有人学编程时都会做。

功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。



'''

import random
target = random.randint(1,100)
number =0
while True:
	cmd = int(raw_input("Please give your guess:"))
	number += 1
	if cmd == target:
		print 'Correct, your round is : ', number
		break
	elif cmd < target:
		print 'the target is bigger'
	else:
		print 'the target is smaller'
