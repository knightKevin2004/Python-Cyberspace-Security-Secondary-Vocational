a="FRPHEVGL"

for i in range(-26,27):
    flag=""
    for j in a:
        if "A"<=chr(ord(j)+i)<="Z":
            flag+=chr(ord(j)+i)
        else:
            flag+=chr(ord(j)+i-26)
    print(i,flag.lower())

flag="ComeChina"
se=""
for i in flag:
    if ord(i)+13>ord("z"):
        se+=chr(ord(i)+13-26)
    else:
        se+=chr(ord(i)+13)
print(se)