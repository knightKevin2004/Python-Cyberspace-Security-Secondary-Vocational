# coding:utf-8

a=[1,2,3]
b=(1,2,3)
c={1,2,3}

print(tuple(a),set(a))
print(type(tuple(a)),type(set(a)))
print(tuple(a) == b)
print(set(a)==c)
print(set(a) is c) #false的原因是因为他们不是相同的内存地址

print(list(b),set(b))
print(list(c),tuple(c))

print(list(a))

print(str(a),type(str(a)))   #'[1,2,3]'
print(str(b),type(str(b)))
print(str(c),type(str(c)))

print(list(str(a)))
print(tuple(str(b)))
print(set(str(c)))   #转换不可逆

_a=str(a)
_b=list(b)
print(_b)