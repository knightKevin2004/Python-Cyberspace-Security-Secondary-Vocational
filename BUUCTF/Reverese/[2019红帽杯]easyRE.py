flag="ACTF{"
key='~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$# !"'
b=[]
c=[]
www="*F'\"N,\"(I?+@"
for i in www:
    b.append(ord(i))
for i in b:
    c.append(key.find(chr(i))+1)
for i in c:
    flag+=chr(i)
flag+="}"
print(flag)

print("#######################################")

v17=[0]*36
v17[0] = 73
v17[1] = 111
v17[2] = 100
v17[3] = 108
v17[4] = 62
v17[5] = 81
v17[6] = 110
v17[7] = 98
v17[8] = 40
v17[9] = 111
v17[10] = 99
v17[11] = 121
v17[12] = 127
v17[13] = 121
v17[14] = 46
v17[15] = 105
v17[16] = 127
v17[17] = 100
v17[18] = 96
v17[19] = 51
v17[20] = 119
v17[21] = 125
v17[22] = 119
v17[23] = 101
v17[24] = 107
v17[25] = 57
v17[26] = 123
v17[27] = 105
v17[28] = 121
v17[29] = 61
v17[30] = 126
v17[31] = 121
v17[32] = 76
v17[33] = 64
v17[34] = 69
v17[35] = 67
flag1=[]
for i in range(36):
    for key in range(32,127):
        if key ^ i == v17[i]:
            flag1.append(chr(key))
print(''.join(flag1))

print("#######################################")

key2=[0x40,0x35,0x20,0x56,0x5D,0x18,0x22,0x45,0x17,0x2F,0x24,0x6E,0x62,0x3C,0x27,0x54,0x48,0x6C,0x24,0x6E,0x72,0x3C,0x32,0x45,0x5B]
key3='flag'
key4=[]
flag=[]
for x in range(4):
    key4.append(chr(key2[x] ^ ord(key3[x])))
print(key4)
for i in range(25):
    flag.append(chr(key2[i]^ord(key4[i%4])))
print(''.join(flag))