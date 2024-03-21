# coding:utf-8

a='abc'
print(a.split())

b='a,b,cd'
print(b.split(','))

c='a|b|c|d'
print(c.split('|',1))
print(c.split('|',2))
#后面的数字代表的是切割的次数

'''
f='a~b~c'
print(f.split(''))
split里面不可以为空字符串的
'''

test=['a','b','c']
test_str='|'.join(test)
print(test_str)

'''
test2=[1,2,3]
print('|'.join(test2))   只要列表里面有任意一个是数字类型的就不能用join
只有字符串才可以用join
'''

sort_str='a b d f i p q c'
sort_list=sort_str.split(' ')
print(sort_list)
sort_list.sort()
print(sort_list)
sort_str=' '.join(sort_list)
print(sort_str)

sort_str_new='abdfipqc'
print(sort_str_new)
res=sorted(sort_str_new)
print(''.join(res))