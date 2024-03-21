import subprocess
import sys
import time
from threading import *

def arping(ip):
    try:
        subprocess.check_output('arping -c 1' + '\t' + str(ip), shell=True)
        time.sleep(1)
        print(ip+":在线")
    except:
        pass

def main():
    host = str(sys.argv[1]).strip()
    addr = host.split('.')[0]+'.'+host.split('.')[1]+'.'+host.split('.')[2]+'.'
    for i in range(1,255):
        ip=addr +str(i)
        t=Thread(target=arping,args=(ip, ))
        t.start()

if __name__=="__main__":
    main()