# coding: utf-8
'''
基于os.path封装的更好用的包

'''
from unipath import Path
if __name__ == '__main__':
    p = Path('/home/real/Script/pytest_new')
    print p.parent  #这是Path实例p的一个属性
    print p.name

