# test_r7_02.py
# coding: utf-8
import prettytable as pt
tb = pt.PrettyTable()
tb.field_names = ["ID", "Command"]
tb.add_row(["1",'SVN update master'])
tb.add_row(["2","SVN restore master"])
tb.add_row(["3", "Start Game Client"])
tb.add_row(["4", "Open master directory"])
tb.add_row(["q","Exit"])
print tb
cmd = raw_input('Give your choice: ')
while cmd !='q':
	
	
	if cmd == '1':
		print 'svn update master'
	elif cmd == '2':
		print 'svn restore master'
	elif cmd == '3':
		print 'start game client'
	elif cmd == '4':
		print 'open master diectory'
	else:
		print 'please give correct choice'
	print tb
	cmd = raw_input('Give your choice: ')