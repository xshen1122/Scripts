# process_srt.py
# coding:utf-8
def check_number(yourstr):
	if yourstr[0] not in ['1','2','3','4','5','6','7','8','9','0']:
		return True
	else:
		return False

def process_srt(filename):
	new_file=[]
	with open(filename,'r') as myfile:
		for line in myfile.readlines():
			if '-->' not in line :
				if check_number(line):
					# print line
					new_file.append(line)
	script_name = filename.replace('srt','txt')
	exist_list  =[]
	with open(script_name,'w') as writefile:
		for item in new_file:
			if item not in exist_list:
				exist_list.append(item)
				writefile.write(item)
	


if __name__ == '__main__':
	filename = '/home/real/SW/Felicity/Felicity.1x01.srt'
	# process_srt(filename)

	process_srt(filename)