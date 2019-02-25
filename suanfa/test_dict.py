# test_dict.py
# coding: utf-8
'''
很灵活，用不好
一、创建字典
二、访问字典里的值
三、修改字典
四、删除字典元素
五、字典键的特性
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
cmp(dict1, dict2) #比较两个字典元素。
len(dict) #计算字典元素个数，即键的总数。
str(dict) #输出字典可打印的字符串表示。
type(variable) #返回输入的变量类型，如果变量是字典就返回字典类型。
radiansdict.clear() #删除字典内所有元素
radiansdict.copy() #返回一个字典的浅复制
radiansdict.fromkeys() #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None) #返回指定键的值，如果值不在字典中返回default值
radiansdict.has_key(key) #如果键在字典dict里返回true，否则返回false
radiansdict.items() #以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys() #以列表返回一个字典所有的键
radiansdict.setdefault(key, default=None) #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2) #把字典dict2的键/值对更新到dict里
radiansdict.values() #以列表返回字典中的所有值

这个例子是我简化过的，我是在一个多线程的程序里发现这个问题的，所以，我的建议是：遍历dict的时候，养成使用 for k in d.keys() 的习惯。
'''