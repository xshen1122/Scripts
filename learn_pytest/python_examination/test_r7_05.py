#test_r7_05.py#
# coding:utf-8
'''
通过adb命令，获取APP的CPU和内存占用，使用pyecharts库，生成测试结果图表

获取内存占用：
adb shell dumpsys meminfo package_name

获取CPU占用：
adb shell cat /proc/pid/stat


'''
from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
print bar.render()
