from scapy.all import *
from threading import Thread


class Saomiao():
    def saomiao(self,ip):
        p=ARP(pdst=ip)
        ans=sr1(p,timeout=1)
        if ans !=None:
            ans.display()
            print(ip,"host is alive.")
        #else:
            #print(ip,"host is died.")

    def main(self):
        for i in range(0,255):
            ip="192.168.3.%s"%i
            t=Thread(target=sm.saomiao,args=(ip,))
            t.start()
            t.join
        
if __name__ == "__main__":
    sm=Saomiao()
    sm.main()