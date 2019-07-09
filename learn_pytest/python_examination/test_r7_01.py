# test_r7_01.py
# coding: utf-8
'''
为了提升效率，设计GM指令模版，需要满足以下几种形式
add_item {{1001 to 1003}},10
add_item {{1001,1003,1006}},10
add_item {{1001 to 1005 not 1002,1003}},10

'''

template = '{{}}'+'time'

class GMCommand(object):
	def __init__(self,cmd):
		self.cmd=cmd
		self.head='add_item '
		
		self.times=''
		

	def find_item(self,yourstr):
		item_list =[]
		number=''
		
		for item in yourstr:
			
			if item.isdigit():
				
				number +=item
			elif item.isdigit()==False:
				if number !='':
					item_list.append(number)
					number = ''
		
		return item_list
	def check_to(self,yourstr):
		if 'to' in yourstr:
			return True
		else:
			return False
	def output_final_list(self,yes_list,flag1, no_list,flag2):
		

		def get_final_list(yourlist,nflag):
			tmp_list =[]
			i=0
			if nflag == True:#(has to)
				while True:
						tmp_list.append(int(yourlist[0])+i)
						i+=1
						if tmp_list[-1] == int(yourlist[-1]):
							break
				return tmp_list
			if nflag==False: #(hasn't to)
				for item in yourlist:
						tmp_list.append(int(item))
				return tmp_list
		# print set(get_final_list(yes_list,flag)).intersection(set(get_final_list(no_list,flag))
		return list(set(get_final_list(yes_list,flag1)).difference(get_final_list(no_list,flag2)))





	def parse_cmd(self):
		yes=''
		no=''
		
		
		
		self.times = (self.cmd.split('}}')[-1])
		yes_list = []
		no_list = []
		if 'not' in self.cmd.split('}}')[0]:
			yes = self.cmd.split('}}')[0].split('not')[0]+'o'
			no = self.cmd.split('}}')[0].split('not')[-1]+'o'
			yes_list = self.find_item(yes)
			no_list = self.find_item(no)
			
			return yes_list, self.check_to(yes), no_list,self.check_to(no)

		else:
			
			
			yes_list = self.find_item(self.cmd.split('}}')[0]+'o')
			return yes_list,self.check_to(self.cmd.split('}}')[0]),[],False




		
	def output(self):
		# print self.parse_cmd()[0]
		# print self.parse_cmd()[1]
		# print self.parse_cmd()[2]
		# print self.parse_cmd()[3]
		# print self.output_final_list(self.parse_cmd()[0],self.parse_cmd()[1],self.parse_cmd()[2],self.parse_cmd()[3])
		
		for item in self.output_final_list(self.parse_cmd()[0],self.parse_cmd()[1],self.parse_cmd()[2],self.parse_cmd()[3]):
			print self.head,item, self.times
		print '================================'
	


if __name__ == '__main__':
	gm = GMCommand('{{1001 to 1003}},10')
	gm.output()
	gm1 = GMCommand('{{1001,1003,1006}},10')
	gm1.output()
	gm2 = GMCommand('{{1001 to 1005 not 1002,1003}},10')
	gm2.output()