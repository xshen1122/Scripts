# calc_bitrate.py
# coding: utf-8
import os
import json
import time
def return_fps_bitrate(filename):
		for item in filename.split('_'):
			if 'M' in item:
				fps = int(item[:-1])
			if 'fps' in item:
				bitrate = int(item[:-3])

		return fps, bitrate

def get_pkt_size(filepath, filename):
	
	
	packetsize_list=[]
	def get_value(str1):
		for item in str1.split(','):
			
			if 'pkt_size' in item:
				return int(item.split(':')[-1][2:-1])
	with open(os.path.join(filepath, filename),'r') as myfile:
		for line in myfile.readlines():
			if 'pkt_size' in line:
				packetsize_list.append(float(get_value(line))*8/40/1000)
				
	# for item in packetsize_list:
	# 	print item
	# average,N = return_fps_bitrate(filename)
	N=24
	average=15
	myfile = open(os.path.join(filepath,time.asctime( time.localtime(time.time()) )+os.path.split(filename)[-1]),'w')
	myfile.write(filename + 'every second bitrate:')	
	for i in range(len(packetsize_list)/N):
		if sum(packetsize_list[i*N:i*N+N])/N > 60:
			str1 = str(i*N/N) + '\t ---> \t' + str((i*N+N-1)) + '\t' +str(sum(packetsize_list[i*N:i*N+N])/N)
			# str1 = str(packetsize_list[i])
			print str1
			myfile.write('\n'+str1)
	# print packetsize_list[0:25]
	myfile.close()


test_dir = '/home/real/cv/ijk/test1'
for item in os.listdir(test_dir):
	if item.endswith('.rmhd') or item.endswith('.mp4'):
		movie_file = os.path.join(test_dir, item)
		

	# movie_file = '/home/real/cv/ijk/die_4K_5M_25fps_v15.4.0_vbv.rmhd'
		filepath = '/home/real/cv/ijk/calc_bitrate'
		if 'rmhd' in movie_file:
			filename = movie_file.replace('rmhd','log')
		if '.mp4' in movie_file:
			filename = movie_file.replace('mp4','log')

		cmd = './ffprobe -show_frames -select_streams v -print_format json=c=1 ' + movie_file + ' > ' + os.path.join(filepath,filename)


		# os.system(cmd)
		print filepath, filename
		get_pkt_size(filepath,filename)

		
