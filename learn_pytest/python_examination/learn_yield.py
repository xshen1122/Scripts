# learn_yield.py
# coding:utf-8
'''
learn what's yield?
'''

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))

def foo1():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)


if __name__ == '__main__':
	
	g = foo()
	print(next(g))
	print("*"*20)
	print(g.send(7))