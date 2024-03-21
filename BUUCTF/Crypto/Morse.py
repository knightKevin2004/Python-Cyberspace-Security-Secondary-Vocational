flag=b"61666374667B317327745F73305F333435797D"

#!/usr/bin python3
#-*-coding=utf-8-*-
import binascii

#若传入的是一连串16进制串，可用以下函数
def hex_to_str1(s):	#s="68656c6c6f"
	s=binascii.unhexlify(s) #unhexlify()传入的参数也可以是b'xxxx'(xxxx要符合16进制特征)
	print(s.decode('utf-8')) #s的类型是bytes类型，用encode()方法转化为str类型

#若传入的是用空格隔开的16进制串，可以用一下函数
def hex_to_str2(s): #s="68 65 6c 6c 6f"
    print("".join([chr(i) for i in [int(b,16) for b in s.split(' ')]])) 


hex_to_str1(flag)