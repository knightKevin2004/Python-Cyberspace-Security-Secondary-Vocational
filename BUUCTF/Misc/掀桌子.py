a="\xc8\xe9\xac\xa0\xc6\xf2\xe5\xf3\xe8\xc4\xef\xe7\xa1\xa0\xd4\xe8\xe5\xa0\xe6\xec\xe1\xe7\xa0\xe9\xf3\xba\xa0\xe8\xea\xfa\xe3\xf9\xe4\xea\xfa\xe2\xea\xe4\xe3\xea\xeb\xfa\xeb\xe3\xf5\xe7\xe9\xf3\xe4\xe3\xe8\xea\xf9\xea\xf3\xe2\xe4\xe6\xf2"
flag=""
for i in a:
    flag+=chr(ord(i)-128)
print(flag)