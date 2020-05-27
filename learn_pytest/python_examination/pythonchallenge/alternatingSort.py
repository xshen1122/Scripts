# alternatingSort.py

def alternatingSort(a):
	b = []
	if len(a)==1:
		return True
	elif len(a)!= len(set(a)):
		return False
	else:
		for i in range(len(a)):
			if i%2==0:
				b.append(a[i/2])
			else:
				b.append(a[-1-i/2])
		print b
		if b==sorted(a):
			return True
		else:
			return False
if __name__ == '__main__':
	# a = [1,3,5,6,4,2]
	a =[-98,-82,-70,-49,58,26,-69,-79,-98]
	print alternatingSort(a)