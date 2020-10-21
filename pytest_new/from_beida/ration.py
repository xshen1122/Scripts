# coding: utf-8
# Module rational defines a class (a type) retional.
# More operations (methods) should be filled.

def gcd(m, n):
    if n == 0 :
        m, n = n, m
    while m != 0 :
        m, n = n%m, m
    return n

class rational :
    def __init__(self, num, den = 1) :
        if type(num) != int or type(den) != int :#检查输入数据num是否为整形，dem是否为整形
            raise TypeError
        if den == 0 : #检查den不能为0
            raise ValueError
        sign = 1
        if (num < 0) :
            num, sign = -num, -sign
        if (den < 0) :
            den, sign = -den, -sign
        g = gcd(num, den)
        # call function gcd defined in rational class.
        self.num = sign * (num//g)
        self.den = den//g

    def print1(self):
        print(self.num, "/", self.den)

    def __str__(self) :#代表打印实例本身
        return str(self.num) + "/" + str(self.den)

    def plus(self, another) :
        den = self.den * another.den
        num = (self.num * another.den +
               self.den * another.num)
        return rational(num, den)

    def __add__(self, another) :
        den = self.den * another.den
        num = (self.num * another.den +
               self.den * another.num)
        return rational(num, den)

    # definitions of other operators/operations
##    ......

x = rational(3,5)
x = x + rational(7,10)
x.print1()
print x
