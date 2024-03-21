users={'name':'dewei','age':33}
for i in users:
    print(i,users[i])

items=users.items()
print(items)

for key,value in users.items():
    print(key,value)

#列表字典
users_list = [
    {'username':'dewei'},
    {'username':'xiaomu'}
]

for user in users_list:
    print(user.get('username'))
    print(user.get('age'))


l =range(6)
print(l,type(l))

for i in l:
    print(i)
#    1 / 0如果上面报错,不会执行else里面的语句
else:
    print('for循环结束了')