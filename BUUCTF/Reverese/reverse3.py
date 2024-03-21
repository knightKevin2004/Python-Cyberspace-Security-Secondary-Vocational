import base64
a='e3nifIH9b_C@n@dH'
flag=""
for i in range(0,len(a)):
    flag+=chr(ord(a[i])-i)
print(flag)
print("flag"+base64.b64decode(flag).decode())