# cp_files.py
# coding:utf-8
import os
import shutil
# import system
def check_duplicate(filename,target):
	known_list = os.listdir(target)
	for item in known_list:
		if item == filename:
			return True
	return False


dirname='/home/real/temp/'
target = '/home/real/temp/new'
file_list = os.listdir(dirname)
for item in file_list:
	if 'nx612345' in item:
		print item
		if check_duplicate(item,target) == False:
		# cmd = 'cp ' + os.path.join(dirname,item) + ' ' + os.path.join(target,item)
		# print cmd
		# os.system(cmd)
		# check current dir, only copy different files.
			shutil.copy(os.path.join(dirname,item),os.path.join(target,item))
