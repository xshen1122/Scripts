# quick_learn_009.py
# coding: utf-8
'''

recur
'''

def f(n):
	if n <=2:
		return n
	else:
		return n*f(n-1)
def p(n):
	if n==1 or n==2:
		return 1
	else:
		return p(n-1)+p(n-2)

if __name__ == '__main__':
	print p(10)