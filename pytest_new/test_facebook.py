# coding: utf-8
'''
list，set，dict,str
感情账本： 和自己有关联的人，情感分数
每一次交往都会改变这个分数
有的加分
有的减分
红名单，白名单

1, 主程序 - 框架
2. 模拟数据
3. 实现功能
'''
import fackbook_data
from cmd.friend_list import show_list, find, find_by_id


def print_usage():
    print '请输入以下命令'
    print 'list:显示名单'
    print 'zhangsan:'
    print '886:quit'

print_usage()





while True:
    cmd = raw_input('your choice:')

    if str(cmd) == '886':
        print 'byebye'
        break
    elif str(cmd) == 'list':
        show_list()
    elif cmd.isdigit():
        find_by_id(cmd)
    else:
        find(cmd)