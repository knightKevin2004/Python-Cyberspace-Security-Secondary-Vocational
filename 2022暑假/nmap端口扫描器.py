#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nmap
import time
import sys

def O(ifO,host):
    try:
        if ifO=='1':
            result = nm.scan(hosts=host,arguments='-O')   #调用nmap执行-O扫描操作系统
            os = result["scan"][host]['osmatch'][0]['name']   # 从返回值里通过切片提取出操作系统版本
            time.sleep(0.1)
            print(host,os)
        elif ifO=='0':
            pass
        else:print("what are you doing")
    except:pass

def rrrport(ifport,host):
    if ifport=='1':
        for proto in nm[host].all_protocols():
            print('protocol : %s' % proto)       
            lport=nm[host][proto].keys()    
            for port in lport:
                print('port:%s\tstate:%s'%(port,nm[host][proto][port]['state']))
    elif ifport=='0':
        pass
    else:print("what are you doing")    

nm = nmap.PortScanner()
a=sys.argv[1]
b=sys.argv[2]
ifport=sys.argv[3]
ifO=sys.argv[4]
b=b.split('.')
b=b[-1]
rhost='%s-%s'%(a,b)
nm.scan(rhost,'1-1000')
for host in nm.all_hosts():
    print(host)
    O(ifO,host)
    rrrport(ifport,host)