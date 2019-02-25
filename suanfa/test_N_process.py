# test_N_process.py
# coding: utf-8
import multiprocessing
'''
# 这个模块的接口和线程模块threading一致
'''
 
 
def add(end, name):
    total = 0
    for i in range(end+1):
        total += i
    print name
    print total
    return total

if __name__ == '__main__':
    # 实例子进程
    ps = multiprocessing.Process(target=add, args=(100, "北门吹雪"), name="北门吹雪")
    # 启动子进程
    ps.start()
    # 等待子进程结束
    ps.join()