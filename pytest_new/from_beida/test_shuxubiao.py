# coding: utf-8

mylist = [1,3,5,8,12]
def search_position(n):
    return mylist[n]
def search_value(value):
    i=0
    while i< len(mylist):
        if mylist[i] == value:
            break
        else:
            i+=1
    if i<= len(mylist):
        return i
def insert(value,position):
    pass

def delete(position):
    pass
if __name__ == '__main__':
    print search_position(2)
    print search_value(5)