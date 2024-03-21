#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scapy.all import *
from scapy.layers.inet import IP,TCP
def saomiao(rhost,rport):
    
    pkt= sr1(IP(dst=rhost)/TCP(dport=rport),timeout=5,verbose=0)
    if pkt==None:
        print(rhost+":"+str(rport)+"IS OPEN")
            
    else:
        print(rhost,rport)
        pass

if __name__ == "__main__":
    for i in range(166,255):
        rhost="192.168.3.%s"%i
        for rport in range(1,65535):
            saomiao(rhost,rport)