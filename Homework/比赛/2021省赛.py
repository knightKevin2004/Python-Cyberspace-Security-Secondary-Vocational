import sys
from scapy.all import RandShort,IP,TCP,sr1,sr
if len(sys.argv)!=4:
    print('Usage:PortScan <IP> <port1> <port2>\n eg:PortScan 192.168.1.1 20 80')
    sys.exit(1)
dst_ip=sys.argv[1]
src_port=RandShort()
for dst_port in range(int(sys.argv[2],int(sys.argv[3])+1):
    packet=IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags="S")
    resp=sr1(packet,timeout=10)
    if(str(type(resp))=="<class 'NoneType'>"):
        print("The port %s is not replied" %(dst_port))
    elif (resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==0x12):
            sr(IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags='AR'),timeout=10)
            print("The port %s is Open" %(dst_port))
        elif (resp.getlayer(TCP).flags==0x14):
            print("The port %s is Closed" %(dst_port))
    else:
        sys.exit(0)