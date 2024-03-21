str="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
text1='TOiZiZtOrYaToUwPnToBsOaOapsyS'
text2='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
flag=''
s=0
for i in range(len(text1)):
    if(i%2==0):
        flag+=text1[i]
    else:
        s=text2.index(text1[i])
        flag+=str[s]
print(flag)