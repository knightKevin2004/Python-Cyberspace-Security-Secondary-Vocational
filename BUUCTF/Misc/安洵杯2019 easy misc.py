# -*- coding:utf-8 -*-
# Author: MoChu7
alphabet = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()\_+-/={}[] "#所有正常打印字符
strings = open(r'E:\Learn\Python\BUUCTF\Misc\11.txt','rb').read()#读取需要统计频数的文本
result = {}
for i in alphabet:
    counts = strings.count(i)
    i = '{0}'.format(i)
    result[i] = counts

res = sorted(result.items(), key=lambda item: item[1], reverse=True)
num = 0
for data in res:
    num += 1
    print('频数第{0}: {1}'.format(num, data))

print('\n---------------以下是频数从多到少的字符，按照从前到后排序---------------')
for i in res:
    flag = str(i[0])
    print(flag[0], end="")

ascii_list = [32,101,116,97,111,110,114,104,105,115,100,108,117,121,103,119]
for i in ascii_list:
    print(chr(i),end="")

code_str = 'etaonrhisdluygw'
code_dict = {'a':'dIW','b':'sSD','c':'adE ','d':'jVf','e':'QW8','f':'SA=','g':'jBt','h':'5RE','i':'tRQ','j':'SPA','k':'8DS','l':'XiE','m':'S8S','n':'MkF','o':'T9p','p':'PS5','q':'E/S','r':'-sd','s':'SQW','t':'obW','u':'/WS','v':'SD9','w':'cw=','x':'ASD','y':'FTa','z':'AE7'}
base_str=''
for i in code_str:
    i = code_dict[i]
    base_str += i
print("\n%s"%base_str)