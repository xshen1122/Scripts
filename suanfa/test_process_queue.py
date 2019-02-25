# test_process_queue.py
# coding: utf-8
import multiprocessing
 
 
def add(ps_queue, end, name, blog):
    total = 0
    for i in range(end+1):
        total += i
    print(name, blog)
    ps_queue.put(total)
 
 
if __name__ == '__main__':
    # 实例队列
    ps_queue = multiprocessing.Queue()
    # 实例子进程
    ps = multiprocessing.Process(target=add, args=(ps_queue, 100, "北门吹雪", "https://www.cnblogs.com/2bjiujiu/"), name="北门吹雪")
    # 启动子进程
    ps.start()
    # 等待子进程结束
    ps.join()
    # 从Queue中取值
    print(ps_queue.get())