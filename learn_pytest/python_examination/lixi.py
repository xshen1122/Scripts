# lixi.py
# AB4100
# coding: utf-8

from tkinter import * 


top = Tk()
L1 = Label(top, text="target_lixi")
L1.pack( side = LEFT)
E1 = Entry(top, bd =20)
E1.pack(side = RIGHT)

L2 = Label(top, text="left_duration")
L2.pack( side = RIGHT)
E2 = Entry(top, bd =20)
E2.pack(side = LEFT)
def calculate(e1,e2):
	target_lixi=float(e1)/100/365
	target_duration=99

	used_duration=target_duration-float(e2)
	original=10000

	'''
	calculate the highest price
	that's the right lixi
	'''

	# print 'the highest price is:', original+original*target_lixi*used_duration
	# print 'still has ', target_duration-used_duration, ' days '
	yourPrice = original*target_lixi*used_duration-9.99
	return round(yourPrice,2), round((target_lixi*target_duration*original-yourPrice)/(target_duration-used_duration)*365/100,3)
	




def on_click():
	str1 = ''
	e1 = E1.get()
	e2 = E2.get()
	s1, s2 = calculate(e2,e1)
	str1 = 'Highest price:' + str(s1) + '  newest lixi ' + str(s2)
	str2 = 'lixi: '+ e1 + ' duration ' + e2
	L3 = Label(top,text="result: "+str1)
	L3.pack(side=RIGHT)


Button(top, text = 'press',command=on_click).pack()
top.mainloop()





#==============================


