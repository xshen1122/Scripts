# coding: utf-8
from collections import Iterable,Iterator
import time
from itertools import islice
'''
问题： 如何实现可迭代对象和迭代器对象？
某软件要求：从网络抓取各个城市的气温消息，并依次显示：
天津： 15-20
北京：17-23等
如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间，我们
期望以“用时访问”的策略，并且能把所有城市气温封装在一个对象里，可用for进行迭代。

1. 实现一个迭代器对象WeatherIterator, next方法每次返回一个城市气温
2. 实现一个可迭代对象WeatherIterable, __iter__方法返回一个迭代器对象

问题：如何使用生成器函数实现可迭代对象？
实现一个可迭代对象的类，他能迭代出给定范围内的所有素数
解决方法： 将该类的__iter__方法实现生成器函数，每次yield返回一个素数


问题：如何进行反向迭代和如何实现反向迭代？
FloatRange(3.0,4.0,0.2)可产生：
正向： 3.0， 3.2， 3.4， 3.6， 3.8， 4.0
反向： 4.0， 3.8， 3.6， 3.4， 3.2， 3.0
方法：
用yield来实现，如果正向：重写__iter__方法，如果反向，重写__reversed__方法

问题：
如何对迭代器做切片操作？
有某个文本文件，如果想取得100-300行的内容。python文本文件是可迭代对象，是否可以f[100:300]?
方法：
使用itertools.islice,他能返回一个迭代对象切片的生成器
f = open('x.txt','r')
islice(f,100,300)


问题：如何在一个for语句中迭代多个可迭代对象？
1. 某班期末考试成绩，语文，英语，数学分别存在三个列表中，同时迭代三个列表，计算总分，并行
2. 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表
统计全学年成绩高于90分人数，串行
方法：
1. 使用内置函数zip，他能够将多个可迭代对象合并，每次迭代返回一个元组
2. 使用itertools.chain, 他可以将多个可迭代对象连接
chinese = []
english=[]
math=[]
for c,m,e in zip(chinese, math, english):
    total.append(c+m+e)
    
e1, e2, e3, e4 = [], [], [], []
for x in chain(e1,e2,e3,e4):
    print x
'''
import requests
# def getWeather(city):
#     # r = requests.get('http://wthrcdn.etouch.cn/weather_min?city=' + city)
#     # data =r.json()['data']['forcast'][0]
#     if city == u'北京':
#         low='20'
#         high='25'
#     elif city == u'上海':
#         low = '30'
#         high = '35'
#     elif city == u'长春':
#         low = '30'
#         high = '35'
#
#
#     return city, low , high

class WeatherIterator(Iterator): #构建自己的可迭代器，主要是显现next方法
    def getWeather(self,city):
        # r = requests.get('http://wthrcdn.etouch.cn/weather_min?city=' + city)
        # data =r.json()['data']['forcast'][0]
        if city == u'北京':
            low = '20'
            high = '25'
        elif city == u'上海':
            low = '30'
            high = '35'
        elif city == u'长春':
            low = '10'
            high = '15'

        return city, low, high
    def __init__(self,cities):
        self.cities = cities
        self.index=0
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)

class WeatherIterable(Iterable): #构建自己的可迭代对象，主要是实现__iter__方法
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities) #返回一个可迭代对象


# for x in WeatherIterable([u"北京",u"上海",u"长春"]):
#     print x

#例子2：利用yield来实现素数的可迭代器
class PrimeNumber(Iterable):
    def __init__(self,start, end):
        self.start = start
        self.end = end

    def isPrime(self,num):
        if num<2:
            return False
        for i in range(2, num):
            if num%i == 0:
                return False
        return True
    def __iter__(self):
        for i in range(self.start, self.end+1):
            if self.isPrime(i):
                yield i
#例子3，浮点数迭代器
class FloatRange():
    def __init__(self,start, end, step=0.1):
        self.start = start
        self.end = end
        self.step=step

    def __iter__(self):
        t=self.start
        while t<=self.end:
            yield t
            t +=self.step

    def __reversed__(self):
        t=self.end
        while t>= self.start:
            yield t
            t -= self.step


if __name__ == '__main__':
    # start_time = time.time()
    for x in PrimeNumber(1,100):
        print x
    #     pass
    # end_time = time.time()
    # print 'execute time is : ', end_time-start_time

    for x in reversed(FloatRange(12.4, 22.0, 0.2)):
        print x