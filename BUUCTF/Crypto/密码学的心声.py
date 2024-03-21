s = '111 114 157 166 145 123 145 143 165 162 151 164 171 126 145 162 171 115 165 143 150'
tmp = [s.split(' ')[i] for i in range(len(s.split(' ')))]
cipher = ''
for i in tmp:
    cipher += chr(int(i,8))
flag = "flag{"+cipher+"}"
print(flag)

l = [111,114,157,166,145,123,145,143,165,162,151,164,171,126,145,162,171,115,165,143,150]
res = ''
for i in l:
    i = str(i)
    res += chr(int(i,8))
 
print(res)