import hashlib

ops = '?My_Aut0_PWN@R0Pxx@@AAEPADPAE@Z'
result = [''] * 31
index = [15, 16, 7, 17, 18, 8, 3, 19, 20, 9, 21, 22, 10, 4, 1, 23, 24, 11, 25, 26, 12, 5, 27, 28, 13, 29, 30, 14, 6, 2, 0]

for i in range(len(ops)):
    result[index[i]] += ops[i]
    
ss = ''.join(i for i in result)
print(ss)
print(hashlib.md5(ss.encode('utf-8')).hexdigest())
#63b148e750fed3a33419168ac58083f5