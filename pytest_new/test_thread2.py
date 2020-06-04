# coding: utf-8
'''

该程序只能在python3下执行，否则multiprocessing 没有spawn，multiprocessing.set_start_method报错
'''
import time
import logging
import multiprocessing

#Do basic configuration for the logging system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [*] %(message)s"
)

import time
import random

from multiprocessing import current_process, freeze_support
import multiprocessing
#current_process: Return process object representing the current process

#freeze_support:Check whether this is a fake forked process in a frozen executable.
#If so then run code specified by commandline and exit.


def worker(task_queue, output):
    for func, args in iter(task_queue.get, 'STOP'):
        result = calculate(func, args)
        output.put(result)


def calculate(func, args):
    result = func(*args)
    # return f'{current_process().name} 操作 {func.__name__}{args} = {result}'
    txt = current_process().name + func.__name__ + str(args) + str(result)
    return txt

# 乘法
def mul(a, b):
    time.sleep(0.5 * random.random())
    return a * b


# 加法
def add(a, b):
    time.sleep(0.5 * random.random())
    return a + b


def main(ctx):
    NUMBER_OF_PROCESSES = 4
    TASKS1 = [(mul, (i, 7)) for i in range(20)]  # 20个乘法运算
    TASKS2 = [(add, (i, 8)) for i in range(10)]  # 10个加法运算

    task_queue = ctx.Queue()  # 乘法运算队列（不是固定的乘法运算操作队列，下面代码也会加入加法运算操作）
    result_queue = ctx.Queue()

    # 乘法运算加入队列-----------------------------------------------------------------------------
    for task in TASKS1:
        task_queue.put(task)
    for i in range(NUMBER_OF_PROCESSES):
        ctx.Process(target=worker, args=(task_queue, result_queue)).start()
    print("获取乘法运算的结果：----------------------[*]")
    # 获取乘法运算的结果---------------------------------------------------------------------------
    for i in range(len(TASKS1)):
        print('\t', result_queue.get())

    # 加法运算加入队列-----------------------------------------------------------------------------
    for task in TASKS2:
        task_queue.put(task)
    print("获取加法运算的结果：----------------------[*]")
    # 获取加法运算的结果---------------------------------------------------------------------------
    for i in range(len(TASKS2)):
        print('\t', result_queue.get())

    # 让四个子进程停止遍历队列---------------------------------------------------------------------
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')


if __name__ == '__main__':
    freeze_support()
    # windows 启动方式
    multiprocessing.set_start_method('spawn')
    # 获取上下文
    ctx = multiprocessing.get_context('spawn')
    main(ctx)
