# test_pillow.py
# coding: utf-8
'''
1. find the same part set(list1) & set(list2)
求两个list的差集、交集与并集的方法

'''
l = [1, 2, 3, 5]
l_one = [2, 8, 6, 10]
print set(l) & set(l_one)
ret = list(set(l) & set(l_one))
print ret # 交集

print list(set(l).union(set(l_one))) # 并集

print list(set(l).difference(set(l_one))) # 差集