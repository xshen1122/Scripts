# coding: utf-8
'''
第二个例子交通等那个太简单，说明不了问题
引入第三个例子

'''
import threading
import time
import random

L = []


def read():
    count = 2
    while 1:
        count = random.randint(0, 1)
        if count:
            L.append('Hello, darling,I love you\n')
            L.append('You are so sweet~\n')
        if L:
            evt.set() #设立标志位，单方向的，read通知parse解析。
            print 'new rcvd sent to \'parse thread\'\n'
        time.sleep(2)
    print 'never here\n'

def parse_my():
    while True:
        evt.wait()
        print 'run parse here\n'
        evt.clear()


def parse():
    while 1:
        if evt.isSet():
            evt.clear()
            print repr(len(L)) + ' messages to parse:\n'
            while L:
                print L.pop(0)
            print 'all msg prased,sleep 2s\n'
            time.sleep(2)
        else:
            print 'no message rcved\n'
            time.sleep(2)
    print 'quit parse\n'


if __name__ == '__main__':
    evt = threading.Event()
    R = threading.Thread(target=read)
    P_my = threading.Thread(target=parse_my)
    R.start()
    P_my.start()
    time.sleep(2)
    # P.start()
    # time.sleep(2)
    # R.join()
    # P.join()
    # time.sleep(2)
    print 'end'
