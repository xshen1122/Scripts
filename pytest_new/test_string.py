# coding: utf-8
'''
问题：如何拆分含有多种分隔符的字符串？
比如含有<,>, <|>, \t等，如何处理？

方法：
1. 连续使用split()方法，每次处理一种分隔符号
2. 使用正则表达式re.split(),一次性拆分字符串-推荐
re.split('[,;\t|]+', s)

利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
注意不要调用str的strip()方法：

说明：
trim是一个用切片方法完成的函数。
迭代器：
那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
isinstance('abc', Iterable)

请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):

为什么需要生成器？
通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。

问题：
如何判断字符串a以字符串b开头或者结尾？
startswith
endswith
多个匹配时参数使用元组。。。
s.startswith(('.py', '.sh'))

问题：如何调整字符串中文本的格式？
方法
使用正则表达式re.sub()方法做字符串替换，利用正则表达式捕获组
捕获每个部分内容，再替换字符串中调整各个捕获组的顺序
print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)


问题：如何将小字符串拼接成大字符串？
方法：
1. 使用+号， 开销浪费
2. 使用str.join()，更加快速的拼接列表中的所有字符串
''.join([s1,s2]), 不适用任何连接符，join的参数是一个列表或者是生成器


问题：如何对字符串进行左，右，居中对齐
方法1： 使用字符串的str.ljust(), str.rjust()， str.center()
方法2： 使用format()方法，传递类似<20, >20, ^20

问题：如何去掉字符串中不需要的字符？
方法1： strip(), lstrip(), rstrip()
'''
import re
def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    elif len(L)==1:
        return (L[0],L[0])
    else:
        big=L[0]
        small=L[0]
        for x in L:
            if x>big:
                big=x
            if x<small:
                small=x



        return (small, big)


def trim(s):
    def isempty(s):
        for x in s:
            if x.isspace()==False:
                return False
        return True
    #判断字符串没有长度？
    if len(s)==0:
        return ''
    #判断字符串全空？
    elif isempty(s):
        return ''

    else:#其他情况，从开始找第一个非空字符位置start，从最后找第一个非空位置end
        i=0
        while s[i]==' ':
            i+=1
        start = i #开头空格
        print start
        i=1
        while s[-i]==' ':
            i+=1
        end = i-1#结尾空格
        print end
        if end ==0:
            return s[start:]

        return s[start:-end]


if __name__ == '__main__':


    # if trim('hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  world  ') != 'hello  world':
    #     print('测试失败!')
    # elif trim('') != '':
    #     print('测试失败!')
    # elif trim('    ') != '':
    #     print('测试失败!')
    # else:
    #     print('测试成功!')

    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
