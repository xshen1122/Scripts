# coding: utf-8
import requests
# from pip._vendor.requests.models import Response


url = 'http://t.weather.sojson.com/api/weather/city/101030100'
r=requests.get(url)
resp = r.json()
print r.text