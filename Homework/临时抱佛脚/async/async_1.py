# coding:utf-8

import time
import os
import random
import asyncio
import gevent

def gevent_a():
    for i in range(10):
        print(i,'a gevent',os.getpid())
        gevent.sleep(random.random()*2)
    return 'gevent a result'

def gevent_b():
    for i in range(10):
        print(i,'b gevent',os.getpid())
        gevent.sleep(random.random()*2)
    return 'gevent b result'

async def a():
    for i in range(10):
        print(i,'a %s' % os.getpid())
        await asyncio.sleep(random.random()*2)
    return 'a function'

async def b():
    for i in range(10):
        print(i,'b %s' % os.getpid())
        await asyncio.sleep(random.random()*2)
    return 'b function'

async def main():
    result=await asyncio.gather(
        a(),
        b()
    )
    print(result)

if __name__=='__main__':
    start=time.time()
    asyncio.run(main())
    print(time.time()-start)
    print('parent is %s' % os.getpid())