# coding: utf-8
from LCList import LCList
'''
设有n 个人围坐一圈，现在从第k 个人开始报数，报到第m 的人退出。
然后继续报数，直至所有人退出。输出出列人顺序编号

'''

def JosephusA(n, k, m):
    people = list(range(1, n+1))
    print '有若干个人围成一圈', people
    num, i = 0, k-1
    for num in range(n):
        count = 0
        print '这是第几轮', num
        print '圈里还剩下多少人', people
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print '第',people[i],'个人退出'
                people[i] = 0
            i = (i+1) % n
        # if num < n-1:
        #     print(", ")
        # else:
        #     print("")
    return

def JosephusL(n, k, m):
    people = list(range(1, n+1))
    if k < 1 or k > n:
        raise ValueError

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m-1) % num
        print(people.pop(i))
        if num > 1:
            print(", ")
        else:
            print("")
    return

class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.isEmpty():
            self.turn(m-1)
            print(self.pop())
            if not self.isEmpty():
                print(", ")
            else:
                print("")
# end class Josephus

if __name__ == '__main__':
    # s = input("Josephus parameters (n k m): ")
    # n, k, m = map(int, s.split())
    n,k,m=10,2,7
    # JosephusA(n, k, m)
    # JosephusL(n, k, m)
    Josephus(n, k, m)

