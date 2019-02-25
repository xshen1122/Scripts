# test_book_words.py
# coding: utf-8
from collections import Counter
filename = 'name.txt'
ct = Counter()
word_list = []
with open(filename, 'r') as myfile:
	for line in myfile.readlines():
		for item in line.split(' '):
			word_list.append(item)

		
print word_list
for item in word_list:
	ct[item] += 1

print ct
print sorted(ct.items(),key=lambda ct:ct[1], reverse=True)