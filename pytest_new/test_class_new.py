# coding: utf-8
import os
import sys
from UserDict import UserDict
'''
书上的例子，有几个重点
1. 继承
2. 列表推导
3. 类的调用
4. 字典UserDict的继承，重写__setitem__, 等同于dict[key]=value
5. 第三层子类： 
MP3FileInfo 是 FileInfo 的子类。在设置了一个 MP3FileInfo 类的 name 时,并
不只是设置 name 关键字 (像父类 FileInfo 所做的),它还要在文件自身内进行搜
索 MP3 的标记然后填充一整套关键字

现在真正有趣的开始了。设置 mp3file 的 name 关键字触发了 MP3FileInfo 上
的 __setitem__ 方法 (而不是 UserDict 的),这个方法注意到我们正在用一个
真实的值来设置 name 关键字,接着调用 self.__parse 。尽管我们完全还没有
研究过 __parse 方法,从它的输出你可以看出,它设置了其它几个关键字:
album 、 artist 、 genre 、 title 、 year
和 comment 。

'''

def stripnulls(data):
    "strip whitespace and nulls"
    return data.replace("\00", "").strip()

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):
    "store ID3v1.0 MP3 tags"
    tagDataMap = {"title" : ( 3, 33, stripnulls),
    "artist" : ( 33, 63, stripnulls),
    "album" : ( 63, 93, stripnulls),
    "year"  : ( 93, 97, stripnulls),
    "comment" : ( 97, 126, stripnulls),
    "genre" : (127, 128, ord)}

    def __parse(self, filename):
        "parse ID3v1.0 tags from MP3 file"
        # print 'filename',filename

        self.clear()
        try:

            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
                if tagdata[:3] == "TAG":
                    for tag, (start, end, parseFunc) in self.tagDataMap.items():
                        self[tag] = parseFunc(tagdata[start:end]) #在这里调用了__setitem__
        except IOError:
            pass
    '''
    __setitem__(self,key,value):

    这个方法应该以与键相关联的方式存储值，以便之后能够使用__setitem__来获取。
    当然，这个对象可变时才需要实现这个方法。
    '''
    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)#在这里调用__parse(),将item作为参数传入=filename，字符串


        FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f)  for f in fileList  if os.path.splitext(f)[1] in fileExtList]


    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
        "get file info class from filename extension"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList] #这里是一处坑，两个f的调用，返回的是instance

if __name__ == '__main__':
   # for info in (listDirectory('/home/real/Script/pytest_new/music',['.mp3'])):
   #     print info

    # for info in listDirectory("/home/real/Script/pytest_new/music", [".mp3"]):
    #
    #      #Python中调用类的方法，必须与实例绑定，或者调用自身.
    #     print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
    mp3 = '/home/real/Script/pytest_new/music/razorback.mp3'
    # fileinfo = FileInfo(mp3)  #获取了一个字典，key为name，value为文件名
    # print fileinfo
    # mp3new = MP3FileInfo(fileinfo)
    # print mp3new
    mp3file = MP3FileInfo()

    mp3file["name"] = mp3
    print mp3file
    print type(MP3FileInfo), type(MP3FileInfo.tagDataMap), type(mp3file)
    print MP3FileInfo.tagDataMap
