# learn_data_name.py
# coding: utf-8

import pandas as pd  
import numpy as np 
# names1880 = pd.read_csv('yob1880.txt',names=['name','sex','births'])
# # print type(names1880)
# t1=names1880.groupby('sex').births.sum()

pieces=[]
names=['name','sex','births']
years = ['1880','1881','1882']
for year in years:
	path = 'yob'+year+'.txt'
	frame=pd.read_csv(path,names=names)
	frame['year']=year
	pieces.append(frame)
names=pd.concat(pieces,ignore_index=True)  # combine multiple DataFrames.


total_births = names.pivot_table('births',index='year',columns='sex',aggfunc='sum')

def add_prop(group):
	births=group.births.astype(float)
	group['prop']=births/births.sum()
	return group

names = names.groupby(['year','sex']).apply(add_prop)


np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)
names.sort_values('prop',ascending=False).head()

def get_top1000(group):
	return group.sort_index(by='births',ascending=False)[:1000]
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
