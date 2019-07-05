# test_r5_01.py
# coding: utf-8
'''
api test

'''
import requests

r= requests.get('http://youdao.com/')
print r.text.encode('utf-8')  # has chinese

r1 = requests.get('http://zzk.cnblogs.com/s/blogpost?Keywords=yoyoketang')
print r1.text.encode('utf-8')