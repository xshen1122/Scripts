# level1.py
from string import maketrans 
str1 = ''' g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.    '''
new_str = ''
for item in str1:
	if item == 'k':
		print 'change k'
		new_str += 'm'
	elif item == 'o':
		print 'change o'
		new_str += 'q'
	elif item == 'e':
		print 'change e'
		new_str += 'g'
	else:
		new_str += item

print new_str 

from_str = 'abcdefghijklmnopqrstuvwxyz'
to_str = 'cdefghijklmnopqrstuvwxyzab'
transform = maketrans(from_str,to_str)
result = str1.translate(transform)
url='map'
result1 = url.translate(transform)
print result
print result1