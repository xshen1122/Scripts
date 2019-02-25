# test_combine_sort.py
# coding:utf-8
'''
思路
注意：A列表和B列表都是已经排序完成的。

有两个list A，B，内含a1，a2，a3，a4，b1，b2,b3,b4
先取a1和b1对比，小的拿出来（比如是a1），在比较b1和a2
直到最后从小到大排列出来

需要考虑每个list的最后一个元素的处理。（没办法pop了）


'''
def combine_sort(l1,l2):
	total_list=[]
	tmp1 = l1.pop()
	tmp2 = l2.pop()

	while len(l1)!=0 or len(l2)!=0:
		
		if tmp1 < tmp2:
			total_list.append(tmp1)
			tmp1 = l1.pop()
		else:
			total_list.append(tmp2)
			tmp2 = l2.pop()
		print tmp1, tmp2, l1, l2

	print tmp1, tmp2	
	if tmp1<tmp2:
		total_list.append(tmp1)
		total_list.append(tmp2)
	if tmp2<tmp1:
		total_list.append(tmp2)
		total_list.append(tmp1)

	return total_list
		




if __name__ == '__main__':
	l1 = [1,3,5,7]
	l2 = [2,4,6,8]
	l1.reverse()
	l2.reverse()
	print combine_sort(l1,l2)