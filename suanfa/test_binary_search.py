# test_binary_search.py
# coding: utf-8
def binary_search(list1, num):
	low = 0
	high = len(list1)-1
	while low<=high:
		mid = (low + high)/2
		guess = list1[mid]
		if guess == num:
			return mid
		if guess > num:
			high = mid-1
		if guess < num:
			low = mid +1
	return None



if __name__ == '__main__':
	list1 = [1,2,3,4,5,6,7,8,9,10,13,16,18,21]
	print binary_search(list1,23)

# 128 O(log2 128), vs O(log2 256)