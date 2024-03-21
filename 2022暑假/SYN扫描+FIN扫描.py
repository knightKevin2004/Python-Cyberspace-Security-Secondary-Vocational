#!/usr/bin/python
# -*- coding: UTF-8 -*-
from scapy.all import *
from scapy.layers.inet import IP,TCP,ICMP


class Saomiao():
    def syn_saomiao(self,rhost,rport):
        try:
            p=IP(dst=rhost)/TCP(dport=int(rport))
            ans=sr1(p,timeout=1,verbose=1)
            if ans[TCP].flags=='SA':
                print(rhost,"port",rport,"is open.")
            else:   
                pass

        except:
            pass
            
    #FIN scanning
    def fin_scan(self,rhost,rport):
        try: 
            res=sr1(IP(dst=rhost)/TCP(dport=rport,flags="F"),timeout=0.1,verbose=0)
            if res == None :
                print(rhost,str(rport)+"is open")
            elif res.haslayer(TCP) :
                if res.getlayer(TCP).flags == 0x14:
                    #print(rhost,str(rport)+"is closed")
                    pass
            elif res.haslayer(ICMP):
                if int(res.getlayer(ICMP).type)==3 and int(res.getlayer(ICMP).code) in [1,2,3,9,10,13]:
                    #print(rhost,str(rport)+"is filtered")
                    pass
        except:
            pass



if __name__ == "__main__":
    saomiao=Saomiao()
    rhost="192.168.3.168"
    for rport in range(1,65535):
        saomiao.syn_saomiao(rhost,rport)
        saomiao.fin_scan(rhost,rport)