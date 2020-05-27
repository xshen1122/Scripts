# send_key.py
# coding: utf-8
import os
import time
key_dict = {'left':21, 'right':22, 'enter':23, 'back':4}
for i in range(200):

	cmd = 'adb shell input keyevent ' + str(key_dict['enter'])

	print cmd
	os.system(cmd)
	time.sleep(3*60)

	cmd = 'adb shell input keyevent ' + str(key_dict['back'])
	print cmd
	os.system(cmd)
