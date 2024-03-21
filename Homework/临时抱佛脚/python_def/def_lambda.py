# coding:utf-8

f=lambda:1#不准在lambda后面使用return
result=f()
print(result)

ff=lambda:print(1)
ff()

f1=lambda x,y:x+y
print(f1(1,2))

ff1=lambda x,y=2:x>y
print(ff1(1))

users=[
    {'name':'dewei'},
    {'name':'xiaomu'},
    {'name':'asan'}
]
users.sort(key=lambda x:x['name'])
print(users)