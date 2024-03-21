import math

flag="ACTF{"
a="Qsw3sj_lz4_Ujw@l"

model = []
for i in a:
    model.append(ord(i))

for i in range(16):
    if ord("A")<=ord(a[i])<=ord("Z"):
        flag+=chr(int(ord(a[i])+51-65))
    elif ord("a")<=ord(a[i])<=ord("z"):
        flag+=chr(int(ord(a[i])+79-97))
        math
    else:
        flag+=a[i]

print (flag+'}')