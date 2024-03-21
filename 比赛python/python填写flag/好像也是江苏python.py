import F1
from F2 import F3, F4, F5, sr1, sr

if len(F1.argv)!=4:
    print('Usage:PortScan <IP> <port1> <port2>\n eg:PortScan 192.168.1.1 20 80')
    F1.exit(1)

dst_ip=F1.argv[1]
src_port=F3()

for dst_port in range(int(F1.argv[2]),int(F1.argv[3])+1):
    packet=F4(dst=dst_ip)/F5(sport=src_port, dport=dst_port, F7="S")
    resp=sr1(packet,timeout=10)
    if(str(type(resp))=="<class 'NoneType'>"):
        print("The port %s is not replied" %(dst_port))
    elif (resp.haslayer(F5)):
        if(resp.F6(F5).flags==0x12):
            sr(F4(dst=dst_ip)/F5(sport=src_port, dport=dst_port, F7='AR'),timeout=10)
            print("The port %s is Open" %(dst_port))
        elif (resp.F6(F5).flags==0x14):
            print("The port %s is Closed" %(dst_port))
    else:
        F1.exit(0)

# F1           sys
# F2           scapy.all
# F3,F4,F5     RandShort,IP,TCP
# F6           getlayer
# F7           flags