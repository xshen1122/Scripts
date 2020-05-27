# get_cores.py
# coding: utf-8
import os
os.system('cat nsdk_pftest.log |grep -e "dump cpu: processor" -e "dump mem info" > 1.log')

with open('1.log','r') as myfile:
	cores =0
	num = 1
	for line in myfile:
		if 'processor' in line:
			cores +=1
		else:
			print num, 'time cores is ', cores
			num +=1
			cores =0