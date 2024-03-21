from scapy.all import *
from scapy.layers.l2 import ARP, Ether

for i in range(0,255):
    ganyu="192.168.3.%s"%i
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ganyu)
    ans, unans = srp(pkt, timeout=1)
    for s, r in ans:
        print('success')
        print(r.sprintf('%Ether.src% - %ARP.psrc%'+ganyu))