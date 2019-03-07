# test_100_2.py
# coding:utf-8
'''
一个无序数组里有99个不重复正整数，
范围从1到100，唯独缺少一个整数。如何找出这个缺失的整数？

method2:
创建一个HashMap，以1到100为键，值都是0 。然后遍历整个数组，每读到一个整数，就找到HashMap当中对应的键，让其值加一。

由于数组中缺少一个整数，最终一定有99个键对应的值等于1, 剩下一个键对应的值等于0。遍历修改后的HashMap，找到这个值为0的键。

假设数组长度是N，那么该解法的时间复杂度是O（1），空间复杂度是O（N）。

method3
先把数组元素进行排序，然后遍历数组，检查任意两个相邻元素数值是否是连续的。如果不连续，则中间缺少的整数就是所要寻找的；如果全都连续，则缺少的整数不是1就是100。

假设数组长度是N，如果用时间复杂度为O（N*LogN）的排序算法进行排序，那么该解法的时间复杂度是O（N*LogN），空间复杂度是O（1）。

method4
很简单也很高效的方法，先算出1+2+3….+100的和，然后依次减去数组里的元素，最后得到的差，就是唯一缺失的整数。

假设数组长度是N，那么该解法的时间复杂度是O（N），空间复杂度是O（1）。

题目扩展：一个无序数组里有若干个正整数，范围从1到100，
其中99个整数都出现了偶数次，只有一个整数出现了奇数次（比如1,1,2,2,3,3,4,5,5），如何找到这个出现奇数次的整数？
method2-1
遍历整个数组，依次做异或运算。由于异或在位运算时相同为0，不同为1，因此所有出现偶数次的整数都会相互抵消变成0，只有唯一出现奇数次的整数会被留下。

假设数组长度是N，那么该解法的时间复杂度是O（N），空间复杂度是O（1）。
异或：相同的两个元素a^b的结果为0. 0^a = a

题目第二次扩展：一个无序数组里有若干个正整数，范围从1到100，
其中98个整数都出现了偶数次，只有两个整数出现了奇数次（比如1,1,2,2,3,4,5,5），
如何找到这个出现奇数次的整数？
遍历整个数组，依次做异或运算。由于数组存在两个出现奇数次的整数，所以最终异或的结果，等同于这两个整数的异或结果。这个结果中，至少会有一个二进制位是1（如果都是0，说明两个数相等，和题目不符）。

举个例子，如果最终异或的结果是5，转换成二进制是00000101。
此时我们可以选择任意一个是1的二进制位来分析，比如末位。
把两个奇数次出现的整数命名为A和B，如果末位是1，说明A和B转为二进制的末位不同，
必定其中一个整数的末位是1，另一个整数的末位是0

分治法，找到特征
'''
# method 1
mylist= [1,2,3,4,5,6,7,8,9,10]
unorder_list = [1,4,6,2,9,10,7,5,3]
def method1(mylist,unorder_list):
	for item in unorder_list:
			if item in mylist:
				mylist.remove(item)
	return mylist
# method 2
def method2(mylist,unorder_list):
	mydict={}
	for item in mylist:
		mydict[item]=0
	for item in unorder_list:
		if item in mydict.keys():
			mydict[item]+=1
	for item in mydict.keys():
		if mydict[item]==0:
			return item
def method3(mylist,unorder_list):
	new_list=sorted(unorder_list)
	print new_list
	for i in range(len(new_list)-1):
		if new_list[i+1]-new_list[i] !=1:
			return new_list[i]+1
def method4(mylist,unorder_list):
	total_value=sum(mylist)
	bad_value=sum(unorder_list)
	return total_value-bad_value

def method2_1(mylist):
	result = mylist[0]
	for i in range(1,len(mylist)):
		result = result^mylist[i]
	return result
		

if __name__ == '__main__':
	# print method1(mylist,unorder_list)
	# print method4(mylist,unorder_list)
	new_list =[1,1,2,2,4,4,5,6,6]
	print method2_1(new_list)

	print 3^3^2
