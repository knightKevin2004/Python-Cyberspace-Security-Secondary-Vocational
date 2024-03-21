# coding:utf-8

a='hello xiaomu'
print(a,type(a))

b=b'hello xiaomu'
print(b,type(b))

print(b.capitalize)  #首字母大写
print(b.replace(b'xiaomu',b'dewei'))  #不加b的话会报类型错误.这句话的意思是把xiaomu替换成dewei
print(b[3])  #因为比特是一个二进制流,所以这些索引返回的都是二进制流形式
print(b[:3])
print(b.find(b'x'))


print(dir(b))

'''
c=b'hello 小木'   中文会报错编码格式不对
print(c)
'''
c='hello 小木'
d=c.encode('utf-8')
print(d,type(d))
print(d.decode('utf-8'))