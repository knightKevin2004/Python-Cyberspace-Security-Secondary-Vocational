# coding:utf-8

import re

def had_number(data):
    result=re.findall('\d',data)
    print(result)
    for i in result:
        return True
    return False

def remove_number(data):
    result=re.findall('\D',data)
    print(result)
    return ''.join(result)

def startswith(sub,data):
    _sub='\A%s'%sub
    result=re.findall(_sub,data)
    for i in result:
        return True
    return False

if __name__=='__main__':
    data='i am dewei,i am 33'
    result=had_number(data)
    print(result)
    result=remove_number(data)
    print(result)

    data='hello xiaomu, i am dewei. i am 33 year\'s old'
    print(re.findall('\W',data))

    result=startswith('hell',data)
    print(result)