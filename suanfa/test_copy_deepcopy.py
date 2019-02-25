# test_copy_deepcopy.py
# coding: utf-8
'''
copy()与deepcopy()之间的区分必须要涉及到python对于数据的存储方式。

深复制被复制对象完全再复制一遍作为独立的新个体单独存在。所以改变原有被复制对象不会对已经复制出来的新对象产生影响。 

对于copy而言，只是变量地址变了，指向的内容地址没变（从list能看出）
对于deepcopy而言，不仅变量地址变了，指向的内容也变了（从list能看出）
但是对于cop[1]的整数而言，可能指向的内容没变。
对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址。

'''
import copy
origin = [1, 2, [3, 4]]
#origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print id(cop1), id(cop2), id(origin)
print id(cop1[1]),id(cop2[1]),id(origin[1]) #27996480 27996480 27996480
print id(cop1[2]),id(cop2[2]),id(origin[2]) # 140349757775456 140349757924056 140349757775456