# test_process_pipe.py
# coding: utf-8
import multiprocessing
 
 
def add(phone_one, end, name, blog):
    total = 0
    for i in range(end+1):
        total += i
    print(name, blog)
    # 发送数据，当然也可以接收
    phone_one.send(total)
 
 
if __name__ == '__main__':
    # 实例管道, 类似打电话
    phone_one, phone_two = multiprocessing.Pipe()
     
    # 实例子进程
    ps = multiprocessing.Process(target=add, args=(phone_one, 100, "北门吹雪", "https://www.cnblogs.com/2bjiujiu/"), name="北门吹雪")
    # 启动子进程
    ps.start()
    # 等待子进程结束
    ps.join()
     
    # Pipe中取值
    print(phone_two.recv())