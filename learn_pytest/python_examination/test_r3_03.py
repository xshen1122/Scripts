# test_r3_03.py
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
但这样做，只是让你的程序在运行的过程中显示中文，如果你要将中文字符存储在文件中，或者写入到数据库中，这样的设置是不能满足你的需要

1.11子曰：“父在，观其(1)志;父没，观其行(2);三年(3)无改于父之道(4)，可谓孝矣。”
'''
newfile = open('论语-提取版.txt','w')
myfile = open('论语-网络版.txt','r')
txt = myfile.read()
print txt
print type(txt)
for item in txt:
	if item not in ['(',')'] and item.isdigit() == False:
		newfile.write(item)
newfile.close()
myfile.close()
# for item in txt:
# 	print item.decode("ISO-8859-1").isdigit()
	
# 	if (item.decode("ISO-8859-1")) not in ['1','2','3','4','5','6','7','8','9','0','(',')']:
# 		print item.decode("ISO-8859-1")
# 		newfile.write(item)