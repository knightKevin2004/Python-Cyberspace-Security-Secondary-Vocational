a="gmbhjtdbftbs"

for i in range(40):
    flag=''
    for j in a:
        flag+=chr(ord(j)-i)
    print(flag)