# test_requests.py
# coding: utf-8
import requests
r=requests.get('http://www.google.com/')
print r.status_code
# print r.text
print r.content
print r.url
print r.headers
print r.cookies