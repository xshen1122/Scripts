# coding: utf-8
surname = 'zhang,li,wang,mo,wu,sun,xu,hu,guo,lin'
firstname = 'yi,er,san,si,wu,liu,qi,ba,jiu'
names = []
records = [((1, 'zhangsan'), 'shout', (2,'lisi'),-1)]
add_score_things = 'zang, praise, money, electric, call, help, gift'
reduce_score_things = 'shout, hit, cheat, rape, threat'

import random
def mock_names(surname,firstname):
    surname_list = surname.split(',')
    firstname_list = firstname.split(',')
    for i in range(1000):
        s = random.choice(surname_list)
        f = random.choice(firstname_list)
        names.append((i+1,s+f))
    return names
def mock_records(names):
    # print names
    good_list = add_score_things.split(',')
    bad_list = reduce_score_things.split(',')
    things_list = good_list+bad_list
    for i in range(1000):
        n1 = random.choice(names)
        n2 = random.choice(names)
        while n2[0]==n1[0]:
            n2=random.choice(names)
        thing = random.choice(things_list)
        if thing in good_list:
            score = -1
        else:
            score = 1
        records.append((n1,thing,n2,score))


def mock_data():
    names = mock_names(surname,firstname)
    mock_records(names)

    return names, records