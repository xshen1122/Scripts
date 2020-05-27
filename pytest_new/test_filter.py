# coding: utf-8

from collections import namedtuple
from collections import Counter
from random import randint
from collections import OrderedDict
from collections import deque
from collections import Iterable,Iterator
import re
'''
问题：
如何在列表，字典，集合中根据条件筛选数据
1. 过滤掉列表中的负数
2. 筛选出字典中高于90的项
3. 筛选出集合中能被3整除的数据
方法1： 列表推导或者字典推导
方法2： filter函数

问题：
如何为元组中的每个元素命名，提高程序的可读性
方法1： 使用大写字母命名index
方法2： 使用标准库的collections.namedtuple代替元组


问题：
如何统计序列中元素的出现频度？
1. 随机序列中出现次数最高的三个元素
2. 英文文章中的单词，出现次数最高的10个单词？

方法1： 使用collections的Counter对象
most_common(n), 统计频度最高的n个元素的列表

问题：
如何根据字典中值的大小，对字典中的项目进行排序？
解决方法
利用内置函数sorted
方法1： 利用zip将字典转换为元组,再使用sorted
方法2： 传递sorted函数的key参数


问题：
如何快速找到多个字典中的公共键？
方法：
使用集合的操作，使用字典的viewkyes()方法得到一个字典keys的集合
2. 使用map，得到所有字典的keys集合
3. 使用reduce函数，得到所有字典keys的集合的交集
map(dict.viewkeys(), [s1,s2,s3])
reduce(lambda a,b: a&b, new_list)


问题：如何让字典保持有序？
使用collections的OrderedDict

问题：如何实现用户的历史记录功能（最多n条）
方法：容量为n的队列存储历史记录
使用deque,它是一个双端循环队列
程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入
使用函数pickle.dump(), pickle.load()

问题： 如何实现可迭代对象和迭代器对象？
某软件要求：从网络抓取各个城市的气温消息，并依次显示：
天津： 15-20
北京：17-23等
如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间，我们
期望以“用时访问”的策略，并且能把所有城市气温封装在一个对象里，可用for进行迭代。

1. 实现一个迭代器对象WeatherIterator, next方法每次返回一个城市气温
2. 实现一个可迭代对象WeatherIterable, __iter__方法返回一个迭代器对象

'''
mylist= [3,9,-1,10,20,-2]
positive_list = [x for x in mylist if x>0] #推导式的方法，列表推导
print (positive_list)

mylist1 = [77,89,32,20,33,66]
zhengchu3_list = [x for x in mylist1 if x%3==0]
print (zhengchu3_list)

mydict={'Lilei':79,'Jim':88,'Lucy':92, 'Lisa':88,'Tiya':99,'William':97}
high_list = [item for item in mydict.keys() if mydict[item]>90]
high_dict = { k:v for k,v in mydict.items() if v>90}# 字典解析，字典推导
print (high_dict)

#方法2， filter，过滤
print (filter(lambda x: x>0, mylist)) # 列表解析是filter方式耗时的一半

NAME,AGE,SEX,EMAIL=range(4)

student = ('Jim',16, 'male','jim@gmail.com')
print (student[NAME],student[AGE],student[SEX],student[EMAIL])

Student= namedtuple('Student',['name','age','sex','email'])
s = Student('Koo',20,'male','koo@gmail.com')
print (s.name)

data = [randint(0,20) for _ in range(30)]
print (data)  #重点是获取字典或者是列表
print (Counter(data).most_common(5))

# 读取一个文件
txt = open('coder.txt','r')
new = re.split('\W+',txt.read()) #非常简洁的使用re，正则表达式来分割文档
# print (new)
print (Counter(new).most_common(10))

new_tuple = zip(mydict.values(), mydict.keys())
print (sorted(new_tuple))

sorted(mydict.items(),key=lambda x: x[1])

q=deque([],5)
