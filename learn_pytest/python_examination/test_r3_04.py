# test_r3_04.py
# coding: utf-8
'''
练习2：模仿王者荣耀定义两个英雄类

要求：

    英雄需要有昵称、攻击力、生命值等属性；
    实例化出两个英雄对象；
    英雄之间可以互殴，被殴打的一方掉血


'''
class Hero(object):
	def __init__(self,nickname,attack,life):
		self.nickname=nickname
		self.attack = attack
		self.life = life
	def be_hit(self):
		self.life -= 1
	def hit(self,enemy):
		enemy.life -=1
if __name__ == '__main__':
	zhang_fei = Hero('zhangfei',90,100)
	guan_yu = Hero('guanyu',95,100)
	zhang_fei.be_hit()
	print zhang_fei.life
	guan_yu.hit(zhang_fei)
	print zhang_fei.life