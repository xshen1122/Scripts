# coding: utf-8
from collections import Iterable,Iterator
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
'''
import requests
def getWeather(city):
    # r = requests.get('http://wthrcdn.etouch.cn/weather_min?city=' + city)
    # data =r.json()['data']['forcast'][0]
    if city == u'北京':
        low='20'
        high='25'
    elif city == u'上海':
        low = '30'
        high = '35'
    elif city == u'长春':
        low = '30'
        high = '35'


    return city, low , high

class WeatherIterator(Iterator):
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

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities) #返回一个可迭代对象


# for x in WeatherIterable([u"北京",u"上海",u"长春"]):
#     print x

class PrimeNumber:
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

if __name__ == '__main__':
    for x in PrimeNumber(1,100):
        print x