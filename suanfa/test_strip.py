# test_strip.py
# coding: utf-8
'''
1. strip()
2. replace()
3. isspace()
4. isdigit()
5. count()
6. unpack()
'''
str1 = "0000000   jb51.net 0000000"
print(str1.strip( '0' ).strip()) # 去除首尾字符 0 
 
str2 = "  jb51.net   "  # 去除首尾空格
print(str2.strip())

str1 = "欢迎访问脚本之家www.jb51.net"
print ("脚本之家旧地址：", str1)
print ("脚本之家新地址：", str1.replace("jb51.net", "jbzj.com"))
 
str1 = "this is string example....wow!!!"
print (str1.replace("is", "was", 3))

def foo(x,y):
	print x, y

alist = [1,2]
adict = {'x':1, 'y':2}
foo(*alist)
foo(**adict)