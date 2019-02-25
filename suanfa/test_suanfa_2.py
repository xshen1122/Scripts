# test_suanfa_2.py
# coding: utf-8

'''
need to add 0 in the beginning
'''
def find_smallest(list1):
	small = list1[0]
	small_index=0
	for i in range(1,len(list1)-1):
		if list1[i] < small:
			small = list1[i]
			small_index=i
	return small_index

if __name__ == '__main__':
	l1 = [3,5,1,0,10,9]
	
	new = []
	for i in range(len(l1)):
		smallest = find_smallest(l1)
		new.append(l1.pop(smallest))
		
	print new

