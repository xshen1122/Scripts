# quick_learn_004.py
# coding: utf-8
import numpy
def printTable(tableData):
	max_col=[]
	ar = numpy.array(tableData)
	def change(item, num):
		return ' '* (int(num)-len(item)) + str(item)

	for i in range(len(tableData)):
		max_value=1
		for item in tableData[i]:
			if len(item) > max_value:
				max_value=len(item)
		max_col.append(max_value)

	for i in range(len(tableData[0])):
		
		str1 = ''
		for j in range(len(ar[:,i])):

			str1 += change(ar[j][i],max_col[j]) + ' '
			# str1 += item + ' '
		print str1


			
	


	

if __name__ == '__main__':
	tableData=[['apples','organes','cherries','banana'],
	           ['Alice','Bob','Carol','David'],
	           ['dogs','cats','moose','goose']]		
	printTable(tableData)  # right order