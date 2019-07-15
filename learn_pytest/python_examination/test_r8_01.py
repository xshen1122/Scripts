# test_r8_01.py

'''

'''

import requests
url = 'http://search.51job.com'
res = requests.get(url)
# res.encoding = "gbk"
res.encoding = res.apparent_encoding
html = res.text
# html = res.text.encoding('iso-8859-1').decode('gbk')
with open('a.txt','w') as myfile:
	myfile.write(html)
# print res.encoding
# print res.apparent_encoding