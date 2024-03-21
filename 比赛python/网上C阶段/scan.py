import os,time,re

with open('port.txt','w') as file:
    file.close()

os.system('masscan  -p21,22,445,3306,3389 10.100.0.0/24 --rate 100000 --wait=0 > scan/port.txt')

time.sleep(3)
with open('port.txt','a') as file:
    with open('scan/port.txt','r') as opfile:
        for r in opfile.readlines():
            port = re.findall('port (.*?)/tcp',r)
            ip = re.findall('on (.*?) ',r)
            ip_port = 'ip'+ip[0]+'port'+port[0]+'\n'
            file.write(ip_port)