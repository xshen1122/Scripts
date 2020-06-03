# coding: utf-8
'''
1、创建员工类Employee，属性有姓名name、能力值ability、年龄age
（能力值为100-年龄），功能有doWork（），该方法执行一次，
该员工的能力值-5，创建str方法，打印该员工的信息

2、创建老板类Boss，属性有金钱money,员工列表employeeList（存储员工类对象）
，工作量work,功能有雇佣员工addEmployee()，雇佣后将员工添加至列表中，
雇佣一人money减5000，金额不足时不能雇佣新员工；开始工作startWork(),
工作开始后，依次取出员工列表中的员工开始工作，员工能力值减少的同时总的
工作量work也减少，当工作量work为0时，工作结束，调用endWork
（该方法为Boss类方法，打印员工的能力值信息）方法，如果所有员工使用完后，
依然没有完成工作，则提示老板需要雇佣新员工，并打印剩余工作量

3、创建Boss类对象，默认执行雇佣3个员工，年龄分别为30,40,50，
然后死循环开始工作，直至工作完成。

模拟超市存包柜的存放物品和取出物品操作，存放物品时选择空储物格，
然后分配密码即为存放完成；取出物品时，输入对应的密码，
打开对应的箱门即为取出物品
fenxi:
1.增加私有变量，练习私有变量的使用
2.多处需要进行数据类型转换，如int(),str()等
3.字符串的拼接和截取，截取使用的是切片的方式
4.密码采用了随机密码+位置码的方式，这样既能直接根据密码定位箱子位置，同时避免了随机生成的重复密码问题

本次主要优化了check_cell()方法、save_goods()方法、get_goods_out()方法，
其中get_goods_out()方法改动最大，取消了for循环，提高了查找性能。
'''
import random
class Locker(object):
    def __init__(self):
        self.__cell_num=5
        self.__use =0
        self.__surplus = self.__cell_num
        self.cell=[0]*self.__cell_num
    def show_cell_detail(self):
        print 'total cell num is: ', self.__cell_num

    def get_surplus(self):
        return self.__surplus

    def check_cell(self):
        for i in range(100):
            position ="%02d"%(i)
            if self.cell[i]==0:
                return position #找到第一个可用的

        return -1

    def save_goods(self):
        if self.__surplus >0:
            self.passwd = random.randint(10000, 99999)
            self.cell_save = self.check_cell()
            self.passwd = str(self.passwd) + self.cell_save
            self.cell_save = int(self.cell_save)
            self.cell[self.cell_save] = self.passwd #将密码存进去，密码=随机+位置（00）
            print self.cell[self.cell_save]
            self.__use+=1
            self.__surplus=self.__cell_num - self.__use
            print self.cell_save+1, ' has been opened, the password is:', self.passwd

    def get_goods_out(self,passwd):
        passwd = str(passwd)
        i = int(passwd[5:7])
        if self.cell[i] == passwd:
            print passwd
            self.cell[i]==0
            self.__surplus +=1
            self.__use = self.__cell_num - self.__surplus
            return i
        return -1





class Employee:

    def __init__(self,name, age):
        self.name = name
        self.ability=100-age
        self.age=age

    def doWork(self):
        self.ability -=5  # 这里有点疑问？
    def __str__(self):
        return self.name + ':' + str(self.ability) +':' +str(self.age)

class Boss():
    def __init__(self,money,  work):
        self.money = money
        self.employeeList = []
        self.work = work
    def addEmployee(self,employee):
        if self.money < 5000:
            return 'You cannot add employee'
        self.employeeList.append(employee)
        self.money -=5000

    def startWork(self):
        for item in self.employeeList:
            while item.ability > 0:
                item.doWork()
                self.work -=5
                if self.work<=0:
                    self.endWork()
        self.endWork()
    @staticmethod  #使用类的静态方法，就不需要带参数self了
    def add(a,b):
        return a+b

    def endWork(self):
        if self.work==0:
            print 'the work is well done'
            for item in self.employeeList:
                print item
        else:
            for item in self.employeeList:
                print item
            print self.work
            print 'You need to add new employee'

class Example():
    chart = 0
    @staticmethod
    def add():
        Example.chart +=1
        return Example.chart
    @staticmethod
    def clear():
        Example.chart = 0

class People(object):
    def __init__(self):
        print '__init__'
    def __new__(cls,*args, **kwargs):
        print '__new__'
        return object.__new__(cls,*args, **kwargs)


if __name__ == '__main__':
    lock = Locker()
    while True:
        lock.show_cell_detail()
        surplus = lock.get_surplus()
        print 'surplus is :', surplus
        operation = str(input("1-存放\n2-取出\n0-退出\n请输入对应操作："))

        if operation == "1":
            if surplus != 0:
                lock.save_goods()
            else:
                print("箱已存满，谢谢使用")
                break
        elif operation == "2":
            while True:
                password = input("请输入取件密码：")
                password = int(password)
                out_result = lock.get_goods_out(password)
                if out_result != -1:
                    print out_result + 1, "号箱门已打开，密码已失效，请取出物品，关好箱门"
                    break
                else:
                    print("密码错误，请核对后再输入！")
        elif operation == "0":
            print("欢迎再次光临！")
            break
        else:
            print("请输入正确的操作！")
            continue

    # People()
    # print Example.chart
    # Example.add()
    # print Example.chart
    # print Example.chart
    # Example.add()
    # print Example.chart
    # Example.clear()
    # print Example.chart
    #
    # eList = []
    # eList.append(Employee('Jerry',30))
    # eList.append(Employee('Koko',40))
    # eList.append(Employee('Bob',50))

    # print eList[0], eList[1], eList[2]
    # boss = Boss(100000,800)
    # for item in eList:
    #     boss.addEmployee(item)

    # boss.startWork()
    # print boss.add(10,20) #可以通过实例+静态方法
    # print Boss.add(10,30) #也可以通过类名+静态方法（静态方法理解为一段内存）