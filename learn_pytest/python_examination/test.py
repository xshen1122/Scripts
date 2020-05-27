# test.py
# coding: utf-8
import os
import time
movie_file = '/home/real/cv/ijk/earth_4K_5M_25fps_5525.rmhd'
filepath = '/home/real/cv/ijk/calc_bitrate'
filename = movie_file.replace('rmhd','log')
myfile = open(os.path.join(filepath,time.asctime( time.localtime(time.time()) )),'w')
myfile.write(filename + 'every second bitrate:')

myfile.close()