# test_r4_01.py
# coding: utf-8
'''
two years early, one python script


'''
class Token(object):
	def __init__(self, t, value):
		self.t = t
		self.value = value
	# def __str__(self):
	# 	str1 = 'Token type = ' + self.t + ', Token value = '+ self.value
	# 	return str1

class Interpreter(object):
	def __init__(self,text): # "3+5"
		self.text = text
		self.pos = 0
		self.current_token = None
		self.current_char = self.text[self.pos]
	def advance(self):
		self.pos +=1
		if self.pos > len(text)-1:
			self.current_char = None
		else:
			self_current_char = self.text[self.pos]
	def skip_whitespace(self):
		while self_current_char == ' ' and self.current_char != None:
			self.advance()
	def integer(self):
		result = ''
		while self.current_char != None and self.current_char.isdigit():
			result = result + self.current_char
			self.advance()
		return int(result)
	def get_next_token(self):
		while self.current_char !=None:
			if self.current_char == ' ':
				self.skip_whitespace()
			continue
			if self.current_char.isdigit():
				return Token(INTEGER,self.integer())
			if self.current_char == '+':
				self.advance()
				return Token(PLUS,'+')
			if self.current_char == '-':
				self.advance()
				return Token(MINUS,'-')
			else:
				return Token(EOF,None)
	def eat(self,token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token
		else:
			self.error()
	def expr(self):
		self.current_token = self.get_next_token()
		left = self.current_token
		self.eat(INTEGER)
		op=self.current_token
		if op == '+':
			self.eat(PLUS)
		elif op == '-':
			self.eat(MINUS)
		right = self.current_token
		self.eat(INTEGER)
		return left.value + right.value





if __name__ == '__main__':
	text = '3+5'
	inter = Interpreter(text)
	result = inter.expr()
	print result