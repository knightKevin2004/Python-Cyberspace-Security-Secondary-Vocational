# coding:utf-8

import threading
import random
import time

lists=['python','django','tornado','flask','bs5','requests','uvloop']

new_lists=[]
def work():
    if len(lists) ==0:
        return
    data=random.choice(lists)
    lists.remove(data)
    new_date='%s_new'%data
    new_lists.append(new_date)
    time.sleep(1)


if __name__=='__main__':
    start=time.time()
    t_list=[]
    for i in range(len(lists)):
        t=threading.Thread(target=work)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()
    print('old list',list)
    print('new list',new_lists)
    print('time is %s' % (time.time()-start))