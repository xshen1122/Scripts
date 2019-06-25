# test_niming.py
# coding:utf-8
'''
1. sorted
2. map

'''
l1 = [('a',11),('b',9),('c',13)]
dict1 = {'a':11, 'b':9,'c':13}
print list(map(lambda x: x*x, [1,2,3,4,5]))
# print sorted(l1, key=lambda x: x[1])
print sorted(dict1.items(), key=lambda d: d[1])

# L= list(filter(is_odd, range(1,20)))
L_new = list(filter(lambda x: x%2==1, range(1,20)))
print '---->', L_new