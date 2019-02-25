# test_kuohao.py
# coding:utf-8
'''
例如 3 * {3 +[(2 -3) * (4+5)]} 的括号是匹配的，
而 3 * {3+ [4 - 6}] 的括号是不匹配的。
zhan lai shixian

思路：
还是先弄清楚算法
keypoint
定义左括号和右括号
遍历string，当遇到左括号就append到队列中。
如果遇到右括号，就list1.pop()取出来一个和右括号对比，如果匹配继续做
如果不匹配，返回False


'''

def match(k1,k2):
	if k1=='}' and k2=='{':
		return True
	elif k1==']' and k2=='[':
		return True
	elif k1==')' and k2 == '(':
		return True
	else:
		return False
def test_kuohao(yourstr):
	RIGHT=['}',')',']']
	LEFT=['{','(','[']
	flag = True
	list1 = []
	for item in yourstr:
		if item in LEFT:
			list1.append(item)
		elif item in RIGHT:
			if match(item,list1.pop()):
				flag==True
			else:
				flag==False
				return False
	return True
if __name__ == '__main__':
	str1 = '3 * {3 +[(2 -3) * (4+5)]}'
	str2 = '3 * {3+ [4 - 6}] '
	print test_kuohao(str1)
	print test_kuohao(str2)