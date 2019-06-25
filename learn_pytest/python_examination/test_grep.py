# test_grep.py
import os

def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def list_files(target):
    while 1:
        dir_to_search=yield
        for top_dir,dir,files in os.walk(dir_to_search):
            for file in files:
                target.send(os.path.join(top_dir,file))
@init
def opener(target):
    while 1:
        file=yield
        fn=open(file)
        target.send((file,fn))
@init
def cat(target):
    while 1:
        file,fn=yield
        for line in fn:
            target.send((file,line))

@init
def grep(pattern,target):
    while 1:
        file,line=yield
        if pattern in line:
            target.send(file)
@init
def printer():
    while 1:
        file=yield
        if file:
            print(file)

g=list_files(opener(cat(grep('python',printer()))))

g.send('/test1')

# 协程应用：grep -rl /dir

# tail&grep