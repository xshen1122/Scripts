# learn_data2_movielens.py
# coding: utf-8
'''

'''
import pandas as pd 
unames = ['user_id', 'gender','age','occupation','zip']
users = pd.read_table('users.dat', sep='::',header=None, names=unames)

rnames =['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('ratings.dat',sep='::',header=None, names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('movies.dat',sep='::',header=None, names=mnames)

# print users[:5]
# print ratings[:5]
# print movies[:5]

data = pd.merge(pd.merge(ratings, users),movies)
# print data.ix[0]

# pivot_table() got an unexpected keyword argument 'rows'
# modify, rows ==> index, cols ==> columns

mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')

mean_ratings1 = data.pivot_table('rating',index='genres',columns='gender',aggfunc='mean')
# print mean_ratings1[:10]

ratings_by_title = data.groupby('title').size()
active_ratings = ratings_by_title.index[ratings_by_title > 250]
mean_ratings = mean_ratings.ix[active_ratings]
top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F'] # add a col "diff"
sort_by_diff = mean_ratings.sort_index(by='diff')
# sort_by_diff[:5]
# sort_by_diff[::-1][:5]
rating_std_by_title = data.groupby('title')['rating'].std()
#print rating_std_by_title[:5] # single column
rating_std_by_title = rating_std_by_title.ix[active_ratings]
print rating_std_by_title.sort_values(ascending=False)[:5] # original is "order", changes to "sort_values"