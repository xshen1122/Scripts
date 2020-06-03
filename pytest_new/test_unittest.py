# coding: utf-8
import unittest

import requests

from time import sleep
class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://t.weather.sojson.com/api/weather/city/101030100'
        self.url_error = 'http://t.weather.sojson.com/api/weather/city/101030101'
        self.url_no = 'http://t.weather.sojson.com/api/weather/city'
    def test_tianjin(self):
        r = requests.get(self.url)
        result = r.json()

        self.assertEqual(result['status'], 200)

        self.assertEqual(result['message'], 'success感谢又拍云(http://upyun.com)提供CDN赞助')
        sleep(3)

    def test_weather_para_error(self):
        r = requests.get(self.url_error)

        result = r.json()

        self.assertEqual(result['status'], 400)

        self.assertEqual(result['message'], '获取失败')

        sleep(3)
    def test_weather_para_no(self):
        r = requests.get(self.url_no)

        result = r.json()

        self.assertEqual(result['status'], 404)

        self.assertEqual(result['message'], 'Request resource not found.')

        sleep(3)

    if __name__ == '__main__':
        unittest.main()
