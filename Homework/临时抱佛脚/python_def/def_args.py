def test_args_super(*args,**kwargs):
    if len(args)>=1:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print(('no name'))
    print(args,len(args))
    print(kwargs,len(kwargs))
test_args_super(1,name='dewei')

a=('python','django')
b={'name':'dewei'}
test_args_super(a,b)

def add(a,b=1):
    print(a+b)

add(1,2)
add(1)
add(a=1,b=2)
add(b=2,a=1)
#add(b=2) 报错,因为a是必传参数

def test(a,b=1,*args):
    print(a,b,args)

s=(1,2)
test(1,2,*s)
#test(a=1,b=2,*s)

def test2(*args,a,b=1):
    print(a,b,args)

test2(a=1,b=2,*s)


def test3(a,b=1,**kwargs):#函数里不加* 传参的时候加*
    print(a,b,kwargs)

test3(1,2,name='dewei')
test3(a=1,b=2,name='dewei')
test3(name='dewei',age=33,a=1,b=2)


d={'name':'小木'}
test3(a=1,b=2,**d)
test3(**d,a=1,b=2)
test3(**d,a=1,b=2)#最推荐这种传参方式