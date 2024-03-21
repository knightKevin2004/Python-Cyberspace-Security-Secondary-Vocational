import base64

f=base64.b64decode("ak1w").decode()
e=base64.b64decode("V1Ax").decode()
#print(e,f)

a=chr(90+34)
b=chr(67)
c=chr(int((3*69+141)/4))
d=chr(int((2*(72/9))*4))
flag=a+b+c+d+e+f
print(a,b,c,d)
print(flag)