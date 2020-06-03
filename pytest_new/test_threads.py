# coding: utf-8
'''
通过雅虎网站获取某只股票的csv文件，现在要下载多个csv数据，并转换为xml文件

由于全局解释器锁（GIL）的存在，多线程进行CPU密集型操作并不能提高执行效率，我们修改程序架构：

1. 使用多个DownloadThread线程进行下载（IO操作）

2. 使用一个ConvertThread线程进行转换（CPU密集型操作）

3. 下载线程把下载数据安全的传递给转换线程。
不错
'''
from StringIO import StringIO
from xml_pretty import pretty #2.7无
from threading import Thread
import requests
# from collections import deque
from Queue import Queue
import tarfile
import os
from threading import Event


class TarThreads(Thread):
    def __init__(self,cEvent, tEvent):
        Thread.__init__(self)
        self.count=0
        self.cEvent=cEvent
        self.tEvent=tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname,'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait() #等待转换完成
            self.tarXML() #打包
            self.cEvent.clear() # 清空后重新使用
            self.tEvent.set() # 通知对方可以转换


class DownloadThread(Thread):
    def __init__(self,sid,queue):
        Thread.___init__(self)
        self.sid = sid
        self.url = 'xxxxx'
        self.url %= str(sid).rjust(6,'0')
        self.queue = queue
    def download(self,url):
        response = requests.get(url,timeout=1)
        if response.ok:
            return StringIO(response.content)
    def run(self):
        print 'Download  ', self.sid
        #1
        data = self.download(self.url)
        #2 (sid, data)
        # lock
        # q.append((self.sid, data))
        self.queue.put((self.sid,data))
def ConvertThread(Thread):
    def __init__(self,queue,cEvent,tEvent):
        Thread.__init__(self)
        self.queue=queue
        self.cEvent = cEvent
        self.tEvent = tEvent

    def csvToXml(self,scsv,fxml):
        pass

    def run(self):

        count =0
        #1. sid, data

        while True:
            sid, data = self.queue.get()
            print 'Convert sid', sid
            if sid==-1:
                self.cEvent.set()#通知对方可以打包
                self.tEvent.wait()#等待打包完成
                break
            if data:

                fname = str(sid).rjust(6,'0')+ '.xml'
                with open(fname,'wb') as wf:
                    self.csvToXml(data,wf)
                count += 1
                if count == 5:
                    self.cEvent.set() #通知对方可以打包

                    self.tEvent.wait() #等待打包完成
                    self.tEvent.clear() # 清空可重复使用
                    count = 0


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i,q) for i in range(10)]
    cEvent = Event()
    tEvent = Event()
    tThread = TarThreads(cEvent,tEvent)
    cThread = ConvertThread(q,cEvent,tEvent)
    tThread.start()

    for t in dThreads:
        t.start()

    cThread.start()

    for t in dThreads:
        t.join()
    q.put(-1,None)
