# test_r3_02.py
# coding: utf-8
f1=open("笑傲江湖-网络版.txt","r",encoding="utf-8") 
f2=open("笑傲江湖-字符统计txt","w",encoding="utf-8") 
txt=f1.read() 
d={} 
for c in txt: 
	d[c]=d.get(c,0)+1 #统计字符 
del d[""] #删除空格和换行符 
del d["\n"] 
ls=[] for key in d: #存入列表 
ls.append("{}:{}".format(key,d[key])) 
f2.write(",".join(ls)) #存入csv格式文件 
f1.close() 
f2.close()
