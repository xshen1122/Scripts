# test_decorate.py
# coding:utf-8
'''
background

'''
import time

def get_run_time(timeout):
	def out_wrapper(func):
		def wrapper(*args, **kwargs):

			time1 = time.time()
			r=func(*args, **kwargs)
			print 'this is func', r
			time2 = time.time()
			run_time = time2-time1
			print 'time is ', time2 - time1
			if run_time > timeout:
				print 'run is overtime.'
			return r  # why None here?
		
		return wrapper
	return out_wrapper

@get_run_time(1)
def hello(name):
	time.sleep(1)
	print 'hello, world', name


if __name__ == '__main__':
	r=hello('Day Day Up')
	print r