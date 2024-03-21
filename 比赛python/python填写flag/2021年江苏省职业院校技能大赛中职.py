#!/usr/bin/python3
# -*- coding: utf-8 -*-
from F1 import *
#flag1 = F1
#flag2 = F2
def portScanner(host,port):
    F3:
#flag3 =F3
        s = F4(AF_INET,SOCK_STREAM)
#flag4 = F4
        s.F5((host,port))
#flag5 = F5
        print('[+] %d open' % port)
        s.F6()
#flag6 = F6
    except:
        pass

def F7():
#flag7 = F7
    setdefaulttimeout(1)
    for p in F8(1,F9):
#flag8 = F8
#flag9 = F9
        portScanner('192.168.0.100',p)

if __name__ == '__main__':
    main()
