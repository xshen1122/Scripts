# test_bole_stack_1.py
# coding: utf-8
'''
stack用法实例1， 匹配左右括号，这个用的比较普遍。
思路：
从头到尾遍历，遇到左括号就存在栈里面。
继续往前遍历，遇到右括号，就从栈里面pop出来一个东西，匹配左右，如果左右匹配，则继续，如果不匹配，则return 错误。
直到所有的元素都遍历完了，仍然没有return错误，就return True（说明所有的括号都匹配成功了）

注意一点：最后left_stack里面要完全没有元素，才是左右match。
'''
def compare(k1,k2):
	if k1=='(' and k2 ==')':
		
		return True
	elif k1=='[' and k2 ==']':
		
		return True
	elif k1=='{' and k2 =='}':
		
		return True
	else:
		return False

def check_kuohao(yourstr):
	LEFT =['(','[','{']
	RIGHT=[')',']','}']


	kuohao_stack=[]
	for item in yourstr:

		if item in LEFT:
			kuohao_stack.append(item)
			
		if item in RIGHT:
			
			c1 = kuohao_stack.pop()
			
			if not compare(c1,item):
				
				return 'left is not matched with right'
	if len(kuohao_stack)==0:
		return 'complete match'
	else:
		return 'there are more than 1 kuohao left'


if __name__ == '__main__':
	str1 = '[(3+4)-(5*6)+[1+2+3]+{3/4}}'
	print check_kuohao(str1)
