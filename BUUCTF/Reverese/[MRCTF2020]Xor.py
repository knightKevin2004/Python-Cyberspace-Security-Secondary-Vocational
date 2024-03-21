a='SAWB~FXZ:J:`tQJ"N@ bpdd}8g'
flag=""
for i in range(len(a)):
    flag+=chr((i+1)^ord(a[i]))
print(flag)