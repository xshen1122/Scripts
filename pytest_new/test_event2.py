# coding: utf-8
import threading,time
'''
这是第二个例子，第一个捉迷藏那个没看懂。
红绿灯函数+汽车函数
1. 当count小于10，设置标志位，打印绿灯
2. 当count在10-15之间，清除标志位，打印红灯
3. 当是其他数，count清零

car函数：
1. 判断标志位设立否，如果设立，打印车辆开始行驶
2. 如果没有，打印车辆等待红灯
'''
def light():
    count = 0
    while True:
        if count < 10:
            event.set()           #设置标志位
            print("\033[42;1m ---green light is on \033[0m")
            count += 1
        elif count < 15:
            event.clear()        #清除标志位
            print("\033[41;1m ---red light is on \033[0m")
            count += 1
        else:
            count  = 0
        time.sleep(1)

def car(n):
    while True:
        if event.is_set():     #如果标志位设立了（即绿灯），那么车子就通行
            print("\ncar[ %s ] is running..." % n)
        else:      #如果标志位没有设立（即红灯），那么车子就不通行
            print("the car[ %s ] is waiting for red light..." % n )
        time.sleep(2)

event = threading.Event()

t1 = threading.Thread(target=light) #建立一个红绿灯的线程

t1.start()

for i in range(3):
    t2 = threading.Thread(target=car,args=(i,))#创建3辆车的线程
    t2.start()

