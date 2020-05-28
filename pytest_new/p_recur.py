# coding: utf-8

'''
切大饼问题
q(n)=q(n-1)+n
'''
def q(n):
    if n==0:
        return 1
    else:
        return q(n-1)+n

if __name__ == '__main__':
    print q(4)