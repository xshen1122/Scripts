# test_r6_03.py
# coding: utf-8

'''
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。

在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万

以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆

11	壹拾壹圆

111	壹佰壹拾壹圆

101	壹佰零壹圆

-1000	负壹仟圆

1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.

例如：a=1

则输出：壹圆

'''

def print_bank(value):
	dict1 = {'1':'壹','2':'贰','3':'叁','4':'肆','5':}

	if value==1:
		result = ''
	elif value==2:
		result = 
	elif value==3:


	print result+'圆'

if __name__ == '__main__':
	print_bank(1)