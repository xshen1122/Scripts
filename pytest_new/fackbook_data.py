# coding: utf-8
from collections import OrderedDict
surname = 'zhang,li,wang,mo,wu,sun,xu,hu,guo,lin'
firstname = 'yi,er,san,si,wu,liu,qi,ba,jiu'
names = []
records = [((1, 'zhangsan'), 'shout', (2,'lisi'),-1)]
name_dict ={}
score_dict={} #{zhangsan: {lisi: 5, wangwu: 7}}双层字典
id_dict={} #存放id和names的对应关系


add_score_things = 'zang, praise, money, electric, call, help, gift'
reduce_score_things = 'shout, hit, cheat, rape, threat'

import random
def mock_names(surname,firstname):
    surname_list = surname.split(',')
    firstname_list = firstname.split(',')
    for i in range(100):
        s = random.choice(surname_list)
        f = random.choice(firstname_list)
        names.append((i+1,s+f))
    return names
def mock_records(names):
    # print names
    good_list = add_score_things.split(',')
    bad_list = reduce_score_things.split(',')
    things_list = good_list+bad_list
    for i in range(5000):
        n1 = random.choice(names)
        n2 = random.choice(names)
        while n2[0]==n1[0]:
            n2=random.choice(names)
        thing = random.choice(things_list)
        if thing in good_list:
            score = 1
        else:
            score = -1
        records.append((n1,thing,n2,score))
def build_dict():
    for r in records:
        id = r[2][0]
        if id in name_dict:
            my_records = name_dict[id]
            my_records.append(r)
        else:
            name_dict[id]=[r]  #两个build字典的函数需要仔细看。

def build_id_dict():
    for n in names:
        id_dict[n[0]] = n[1]

def build_score():
    for r in records:
        id = r[2][0]
        action_id = r[0][0]
        if id in score_dict:
            scores = score_dict[id]

            if action_id in scores:
                scores[action_id] += r[3]
            else:
                scores[action_id] = r[3]
        else:
            score_dict[id] = {action_id:r[3]}
    # print 'before:', score_dict[3]
    for id in score_dict:
        scores = score_dict[id] #为什么下面的排序语句单独就可以？妈呀，不能用普通字典。得用OrderedDict
        # print 'before:', scores
        tmp = OrderedDict(sorted(scores.items(), key=lambda nn:nn[1]))
        score_dict[id]=tmp
        # print 'after:', score_dict[3]

        # sorted_scores = {k:v for k,v in sorted(scores.items(),key=lambda nn: nn[1])}
        # print 'this is', sorted_scores
    # score_dict[3]=tmp
    # print 'after: ', score_dict[3]




def mock_data():
    print 'mocking data'
    names = mock_names(surname,firstname)
    mock_records(names)
    build_dict() #将name和records建立对应的字典关系
    build_score()
    build_id_dict()
    print 'mocking data finished'

    # return names, records

mock_data()
# print score_dict[3]
# print score_dict[3]#奇怪，单独debug这条排序语句是对的，但是放到程序里就不对了。

