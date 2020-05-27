# quick_learn_003.py
# coding: utf-8
def displayInventory(yourdic):
	num=0
	for item in yourdic.keys():
		print yourdic[item], item
		num += yourdic[item]
	print 'Total number of items:', num 
def addToInventory(inv,yourlist):
	for item in yourlist:
		if item in inv.keys():
			inv[item]+=1
		else:
			inv[item]=1  # add a key and a value into dic...

	return inv

if __name__ == '__main__':
	dragenRoot=['gold coin','dagger','gold coin','gold coin','ruby']
	inv = {'gold coin':42, 'rope':1}
	inv = addToInventory(inv, dragenRoot)
	displayInventory(inv)


