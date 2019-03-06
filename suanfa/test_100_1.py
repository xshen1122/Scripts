# test_100_1.py
# coding: utf-8
'''

题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？题目没看对(所有的数字都不能重复)
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
'''
choose_list = [1,2,3,4]
comb_list = []
for d3 in choose_list:
	for d2 in choose_list:
		for d1 in choose_list:
			if d1==d2 or d1==d3 or d2==d3:
				pass
			else:
				comb_list.append(d3*100+d2*10+d1)

print 'the result is ', len(comb_list)
print comb_list
