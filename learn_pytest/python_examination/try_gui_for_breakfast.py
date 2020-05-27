# try_gui_for_breakfast.py
# coding: utf-8
from Tkinter import *
import random
import tkMessageBox
top=Tk()
li     = ['Cairoubing','Zhengjiao','Banmian','Zhou','Mianbao','Tangyuan','Danghuangbao','Doujiaomenmian']
# movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(top)          #  创建两个列表组件
# listb2 = Listbox(top)

def helloCallBack():

	tmp = random.randint(0,len(li)-1)
   	tkMessageBox.showinfo( "Hello Python", li[tmp])
B = Button(top, text ="点我", command = helloCallBack)

               # 第一个小部件插入数据
# listb.insert(0,li[tmp])
 
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
 
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
                # 进入消息循环
B.pack()
top.mainloop()
