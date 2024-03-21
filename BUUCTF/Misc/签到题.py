import base64

a=base64.b64decode("Z2dRQGdRMWZxaDBvaHRqcHRfc3d7Z2ZoZ3MjfQ==").decode()
print(a)

flag=""
for i in a:
    if "A"<=i<="Z":
        flag+=chr((ord(i)-ord("A")+12)%26+ord("A"))
    elif "a"<=i<="z":
        flag+=chr((ord(i)-ord("a")+12)%26+ord("a"))
    else:
        flag+=i
flag=flag.lower()
print(flag)