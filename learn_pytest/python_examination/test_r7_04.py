# test_r7_04.py
# coding: utf-8
'''
通过adb，对当前安卓界面进行截图，支持 adb screencap 和 minicap 两个方式，导出截图文件到指定文件夹

支持使用pillow库对截图文件的尺寸进行压缩
screencap

adb shell /system/bin/screencap -p /sdcard/xx.png
adb pull /sdcard/xx.png /home/real/Script/learn_pytest/python_examination/test_apk/

pillow
'''

import os
from PIL import Image
cmd1 = 'adb shell /system/bin/screencap -p /sdcard/xx.png'
cmd2 = 'adb pull /sdcard/xx.png /home/real/Script/learn_pytest/python_examination/test_apk/'

# process xx.png
png_file = '/home/real/Script/learn_pytest/python_examination/test_apk/width_length.png'
im = Image.open(png_file)
print im.size
print round(im.size[0]*0.5), im.size[1]*0.5
print im.mode
print im.info
im.resize((int(im.size[0]*0.5),int(im.size[1]*0.5)),Image.ANTIALIAS).save('/home/real/Script/learn_pytest/python_examination/test_apk/new.png')
