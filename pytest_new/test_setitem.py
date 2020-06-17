# coding: utf-8

class Tag:
    def __init__(self):
        self.change = {'python': 'This is python',
                       'php': 'PHP is a good language'}

    def __getitem__(self, item):
        print('调用getitem')
        return self.change[item]

    def __setitem__(self, key, value):
        print('调用setitem')
        self.change[key] = value


a = Tag()
# print(a['php'])
a['php'] = 'PHP is not a good language'
print(a['php']) #__setitem__在字典赋值的时候调用了。
