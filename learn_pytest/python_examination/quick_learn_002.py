# quick_learn_002.py
# coding: utf-8

def split(yourlist):
	newstr= yourlist[0]
	for item in yourlist[1:-1]:
		newstr = newstr +', ' + item
	newstr = newstr + ' and ' + yourlist[-1]
	return newstr

if __name__ == '__main__':
	l1 = ['apples','bananas','tofu','cats']
	print split(l1)