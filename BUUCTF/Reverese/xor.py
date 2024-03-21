a=[102,10,107,12,119,38,79,46,64,17,120,13,90,59,85,17,112,25,70,31,118,34,77,35,68,14,103,6,104,15,71,50,79]
flag="f"
for i in range(len(a)):
    a[i]=chr(a[i])
a="".join(a)
for i in range(1,len(a)):
    flag+=chr(ord(a[i])^ord(a[i-1]))
print(flag)