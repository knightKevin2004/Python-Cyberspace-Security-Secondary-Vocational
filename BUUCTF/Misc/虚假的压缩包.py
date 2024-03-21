import gmpy2

p=gmpy2.mpz(3)
q=gmpy2.mpz(11)
e=gmpy2.mpz(3)
l=(p-1)*(q-1)
d=gmpy2.invert(e,l)
c=gmpy2.mpz(26)
n=p*q
ans=pow(c,d,n)
print (ans)

import re
import struct

b=""
with open(r"E:\Learn\Python\BUUCTF\Misc\亦真亦假","r") as a:
    a=a.read()
    for i in a:
        tmp = int(i,16) ^ 5
        b += hex(tmp)[2:]

rule=re.compile("..")
hexlist=re.findall(rule,b)

binfile = open(r"E:\Learn\Python\BUUCTF\Misc\complete.doc", 'wb+') ##需要删除之前生成的同名文件
for x in hexlist:
    x = int(x, 16)
    x = struct.pack('B', x)
    binfile.write(x)
binfile.close()