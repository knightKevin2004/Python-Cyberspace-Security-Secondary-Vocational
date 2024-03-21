# coding:utf-8

name='dewei'

def test():
    print(name)

test()

def test1():
    name='小木'
    print('函数体内',name)

test1()
print('函数外',name)


def test5():
    global name
    name=10
    #global先使用

test5()
print(name)

test_dict={'a':1,'b':2}

def test6():
    test_dict['c']=3
    test_dict.pop('a')

test6()
print(test_dict)