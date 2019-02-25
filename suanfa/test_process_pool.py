# test_process_pool.py
# coding:utf-8
import multiprocessing
 
 
def add(end, name, blog):
    total = 0
    for i in range(end+1):
        total += i
    print(name, total, blog)
    return total
 
 
if __name__ == '__main__':
    # 实例子进程，和CPU数量一致
    ps_pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 提交任务，获得返回进程对象对象, 可在此提交多个进程
    r = ps_pool.apply_async(func=add, args=(100, "北门吹雪", "https://www.cnblogs.com/2bjiujiu/"))
    # 获取执行结果，状态信息
    print(r.get())
    # print(r.wait())
    print(r.ready())
    print(r.successful())
    # 关闭线程池
    ps_pool.close()
    # 等待子线程完成
    ps_pool.join()