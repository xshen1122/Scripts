# coding: utf-8
import sys
# sys.path.append('/home/real/Script/pytest_new')
from fackbook_data import *
def show_records(id):
    # my_records = [r for r in records if r[2][0]==id]
    my_records = name_dict[id]
    for r in my_records:
        print r[0], r[1], r[3]


def show_summary(id):
    for sid,score in list(score_dict[id].items())[-1:-6:-1]:
        print id_dict[sid] , '---', score_dict[id][sid]


def find_by_id(id):
    id = int(id)
    persons=[n for n in names if n[0]==id]
    if len(persons)==0:
        print '无效的id'
    else:
        person = persons[0]
        show_one(person)


def show_list():
    for item in names:
        print item

def show_one(person):
    print person[0],' : ', person[1]
    # show_records(person[0])

    show_summary(person[0])

def find(name):
    my_name = [n for n in names if n[1]==name]
    #空
    count = len(my_name)
    if count == 0:
        print 'empty name'
    elif count > 1:
        for n in my_name:
            print n
        print '有多个同姓名的人，请输入id选择具体的人'

    else:
        show_one(my_name[0])
    #多人

