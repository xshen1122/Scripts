# test_r9_03.py
# coding: utf-8
import heapq    #引入堆模块
import random   #产生随机数
test_list = []  #测试列表
for i in range(1000000):                #产生100w个数，每个数在【0,1000w】之间
    test_list.append(random.random()*100000000)
print len(test_list)
print len(set(test_list))
print heapq.nlargest(10,test_list)             #求100w个数最大的10个数
print heapq.nsmallest(10,test_list) #求100w个数最小的10个数