#-*- coding: UTF-8-*-
flag=""
a="1021089710337556653100525310297505354515550505052102525655525499541029856101515198515037556"
while len(a):
    if int(a[:3])<128:
        flag+=chr(int(a[:3]))
        a=a[3:]
    else:
        flag+=chr(int(a[:2]))
        a=a[2:]
flag=flag.encode('UTF-8').decode('UTF-8')
print(flag)