# test_bole_sort.py
# coding:utf-8
'''
1、插入排序

描述

插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。
是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
但将最后一个元素除外（让数组多一个空间才有插入的位置），
而第二部分就只包含这一个元素（即待插入元素）。
在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
实际就是先弄出来一个left_list,先选第一个元素放进去，它就是最小的元素。
然后对剩下的元素一个个的过，如果比left_list的元素小，就插在相应的位置上，如果比left_list的最后一个元素都大，就插在最后。

2、希尔排序

描述

希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，
是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，
算法便终止。

3. 冒泡排序

（Bubble Sort，台湾译为：泡沫排序或气泡排序）是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

步骤：

    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

4. 选择排序(Selection Sort)

选择排序也是一种简单直观的排序算法。
它的工作原理很容易理解：初始时在序列中找到最小（大）元素，
放到序列的起始位置作为已排序序列；
然后，再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

注意选择排序与冒泡排序的区别：
冒泡排序通过依次交换相邻两个顺序不合法的元素位置，
从而将当前最小（大）元素放到合适的位置；
而选择排序每遍历一次都记住了当前最小（大）元素的位置，
最后仅需一次交换操作即可将其放到合适的位置。
'''
def bubble_sort(yourlist):
	for j in range(len(yourlist)-1):
		for i in range(len(yourlist)-1):
			if yourlist[i+1]<yourlist[i]:
				tmp=yourlist[i+1]
				yourlist[i+1]=yourlist[i]
				yourlist[i]=tmp
	return yourlist


def choose_sort(yourlist):
	new_list=[]
	def find_min(yourlist):
		min_data=yourlist[0]
		pos=0
		for i in range(1,len(yourlist)-1):
			if min_data>yourlist[i]:
				min_data=yourlist[i]
				pos = i
		return pos
	for i in range(len(yourlist)):
		p=find_min(yourlist)
		new_list.append(yourlist[p])
		yourlist.pop(p)
	return new_list


def insert_sort(yourlist):
	
	left_list=[]
	left_list.

	ggiggitddd(yourlist[0])
	for i in range(1,len(yourlist)):
		# print 'choose number', yourlist[i]
		 
		for j in range(len(left_list)):
			# print 'j is',j,':',left_list[j]
			if yourlist[i]<left_list[j]:
				if j !=0:
					# print i, 'in level 1'
					left_list.insert(j,yourlist[i])
					break
				elif j == 0:
					# print i, 'in level 2'
					left_list.insert(0,yourlist[i])
					break
		if yourlist[i]>left_list[-1]:
			left_list.append(yourlist[i])
		
		print '=====',left_list
		
	return left_list




if __name__ == '__main__':
	l1 = [3,2,7,5,4,1,0,20,15,12,17,9,6,80]
	
	# print choose_sort(l1)
	l2 = [3,2,7,5,4,1,0,20,15,12,17,9,6,80]
	
	print insert_sort(l2)

	print bubble_sort(l1)