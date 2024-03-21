import hashlib

for i in range(1000,999999):
    fin=str(i)+"@DBApp"
    flag=hashlib.sha1(fin.encode("utf8"))
    flag=flag.hexdigest()
    #print(flag)
    if flag=="6E32D0943418C2C33385BC35A1470250DD8923A9".lower():
        print(fin)
        break

rtf = '{\\rtf1' #\\需要注意，\r需要转义，变成\\r
A = [0x05, 0x7D, 0x41, 0x15, 0x26, 0x01]
password=''
for i in range(len(rtf)):
    x = ord(rtf[i]) ^ A[i]
    password+=chr(x)
print(password)