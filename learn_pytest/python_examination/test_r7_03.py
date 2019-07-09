# test_r7_03.py
# coding: utf-8
'''
遍历文件夹，获取全部的APK文件，依次调用adb install命令安装到测试机中

遍历可以使用 os.walk 函数

有些安卓手机会弹窗确认是否安装，本题可先忽略这个情况，默认为adb install可以静默安装


'''

import os
apk_dir = '/home/real/Script/learn_pytest/python_examination/test_apk'
for roots, dirs, files in os.walk(apk_dir):
	
		for file1 in files:
			if '.apk' in file1:
				cmd = 'adb install ' + os.path.join(roots,file1)
				print cmd

		# for dir1 in dirs:
		# 	print os.path.join(roots,dir1)