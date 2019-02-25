# test_ch04.py
# coding: utf-8
'''
def quicksort

'''
def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i<=pivot]
		greater =[i for i in array[1:] if i > pivot]
		print '---->', quicksort(less) + [pivot] + quicksort(greater)
		return quicksort(less) + [pivot] + quicksort(greater)
if __name__ == '__main__':
	array = [10,5,2,3]
	print quicksort(array)