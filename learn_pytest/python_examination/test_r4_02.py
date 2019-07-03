# test_r4_02.py
# coding: utf-8
'''
'3+5' , tubie
if add * 
'''
if __name__ == '__main__':
	text = '3+5'
	op=''
	left = ''
	right = ''
	for item in text:
		
		if op=='' and item.isdigit():
			
			left=left+item
			
		elif item == '+':
			op = '+'
			

		elif op != '' and item.isdigit():
			right = right+item
	print int(left) + int(right)