# learn_data1.py
# coding: utf-8
'''
learn how to pre-process data


'''
import json
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd  
import numpy as np  
import matplotlib as plot


path = '/home/real/Script/suanfa/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path).readlines()]
print records[0] # every raw...., records is a list. 
# every raw = element is a dict.
print type(records[0]) # 利用json的函数，将txt内的数据转换为字典
# print records
# 3000多个数据中可能有某几行没有'tz' key

# for item in records:
# 	for key in item.keys():
# 		if key=='tz':
# 			print key
# 	print '==========================='
# 单独弄出来8个数据，里面均有tz，为啥还报 KeyError, KeyError = no such key
# 找到了第三个数据是坏的，只有一行，没有tz信息。

time_zones = [rec['tz'] for rec in records if 'tz' in rec] # add a "if" to protect.
print time_zones[:10]
counts=Counter(time_zones[:10])
print counts
print counts.most_common(3)
#=================================================#
frame = DataFrame(records)


clean_tz = frame['tz'].fillna('Missing111')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts() 
tz_counts[:10].plot(kind='barh',rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
print results[:10].value_counts()

cframe = frame[frame.a.notnull()]
cut_frame= cframe[:10]
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print operating_system

by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
print indexer[:10]
count_sub=agg_counts.take(indexer)[-10:]
print count_sub