# quick_learn_001.py
# coding: utf-8
import random

target_value = random.randint(1,10)
print 'target value is', target_value
print 'please input 1-10 number:'
try:
	guess = int(raw_input())
except ValueError:
		print 'your input must be number'

number=1
while guess!=target_value:
	
	if guess > target_value:
		print 'your guess is bigger,guess again:'
		guess = int(raw_input())
		number += 1
	else:
		print 'your guess is smaller,guess again:'
		guess = int(raw_input())
		number +=1
print 'your guess is right, the total guess time is', number
