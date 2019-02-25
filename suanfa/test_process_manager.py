# test_process_manager.py
# coding:utf-8
import multiprocessing
from multiprocessing import Manager
 
 
def add(share_list, end, name, blog):
    total = 0
    for i in range(end+1):
        total += i
    print(name, blog)
    # 添加数据
    share_list.append(total)
    share_list.append(name)
    share_list.append(blog)
 
 
if __name__ == '__main__':
    # 实例共享内存对象
    share_memory = multiprocessing.Manager()
    # 实例list数据类型，当然除了list包括Python基本数据结构
    share_list = share_memory.list()
 
    # 实例子进程
    ps = multiprocessing.Process(target=add, args=(share_list, 100, "北门吹雪", "https://www.cnblogs.com/2bjiujiu/"), name="北门吹雪")
    # 启动子进程
    ps.start()
    # 等待子进程结束
    ps.join()
 
    # 从共享对象中取值
    print(share_list)