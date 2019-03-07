# test_100_4.py
# coding: utf-8
'''
求两个数的最大公约数
辗转相除法， 又名欧几里得算法（Euclidean algorithm），
目的是求出两个正整数的最大公约数。它是已知最古老的算法， 
其可追溯至公元前300年前。
这条算法基于一个定理：两个正整数a和b（a>b），
它们的最大公约数等于a除以b的余数c和b之间的最大公约数。
比如10和25，25除以10商2余5，那么10和25的最大公约数，
等同于10和5的最大公约数。

他的原理更加简单：两个正整数a和b（a>b），它们的最大公约数等于a-b的差值c和较小数b的最大公约数。
比如10和25，25减去10的差是15,那么10和25的最大公约数，等同于10和15的最大公约数。


combine two algorithms
众所周知，移位运算的性能非常快。对于给定的正整数a和b，不难得到如下的结论。其中gcb(a,b)的意思是a,b的最大公约数函数：

当a和b均为偶数，gcb(a,b) = 2*gcb(a/2, b/2) = 2*gcb(a>>1, b>>1)

当a为偶数，b为奇数，gcb(a,b) = gcb(a/2, b) = gcb(a>>1, b)

当a为奇数，b为偶数，gcb(a,b) = gcb(a, b/2) = gcb(a, b>>1)

当a和b均为奇数，利用更相减损术运算一次，gcb(a,b) = gcb(b, a-b)， 此时a-b必然是偶数，又可以继续进行移位运算。


比如计算10和25的最大公约数的步骤如下：

    整数10通过移位，可以转换成求5和25的最大公约数
    利用更相减损法，计算出25-5=20，转换成求5和20的最大公约数
    整数20通过移位，可以转换成求5和10的最大公约数
    整数10通过移位，可以转换成求5和5的最大公约数
    利用更相减损法，因为两数相等，所以最大公约数是5

“>> 右移,高位补符号位” 这里右移一位表示除2“>>> 无符号右移,高位补0”；

 与>>类似“<< 左移” 左移一位表示乘2，二位就表示4，就是2的n次方

原来算法代码上有错误，在最后都是奇数的判定时，应该拿b,a-b(小的数，a-b)而不是a，a-b(大数）
通过打印显示出每一步走的路线，容易找到错误。

'''
def method1(n1, n2):
	result = min(n1,n2)
	for i in range(result,1,-1):
		print i
		if n1%i == 0 and n2%i == 0:
			return i
	return 'no result'
def method2(n1,n2):
	print '====',n1,n2
	if n1==n2:
		return n1
	elif n1<n2:
		return method2(n2,n1)
	else:
		if not n1&1 and not n2&1: #都是偶数
			print 'run level 1'
			return method2(n1>>1,n2>>1)<<1
		elif not n1&1 and n2&1:
			print 'run level2'
			return method2(n1>>1,n2)
		elif n1&1 and not n2&1:
			print 'run level3'
			return method2(n1,n2>>1)
		elif n1&1 and n2&1:  #都是奇数
			print 'run level4'
			return method2(n2,n1-n2)
if __name__ == '__main__':
	# print method1(10000,10001)
	print method2(25,10) #RuntimeError: maximum recursion depth exceeded, need to debug