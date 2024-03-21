import base64

flag="a2FuYmJyZ2doamx7emJfX19ffXZ0bGFsbg=="
flag=base64.b64decode(flag).decode()
print(flag)

for i in range(26):
    i=7
    flag2=[]
    flag3=""
    for x in range(i):
        for j in range(len(flag)):
            if((j+x)%i==0):
                flag2.append(flag[j])
    flag3="".join(flag2)
    print(flag3+"||||||||||||||||||||||||||||"+str(i))
