# luanma.py
# coding: utf-8
import requests

import sys  
  
reload(sys)  
sys.setdefaultencoding('utf8') 

url='http://search.51job.com'
res=requests.get(url)
# print res.text
# print res.encoding

#===method1 ===
res.encoding='gbk'
print res.text

#===method2===
res.encoding=res.apparent_encoding
print res.text


#===method3===
print res.text.encode('iso-8859-1').decode('gbk')