import hashlib
import os

def turnmd5(aaa):
    obj = hashlib.md5()
    obj.update(aaa.encode("utf-8"))
    result=obj.hexdigest()
    return result

def duoshaoti():
    f=open("C:\\Users\\Kevin\\Desktop\\答案.txt")
    lines = len(f.readlines())
    number=lines/2-1
    return number
    
if  __name__ == '__main__':
    score=0
    i=0
    number=duoshaoti()
    while i<=number:
        with open("C:\\Users\\Kevin\\Desktop\\答案.txt","r") as fin:
            n_lines=0
            for answer in fin:
                n_lines +=1
                
                if n_lines%2==0:
                    aaa=str(input("你的答案会是什么"))
                    
                    md5=str(turnmd5(aaa))
                    #print(1)
                    if md5==answer.replace("\n",""):
                        #print(answer)
                        #print(md5)
                        #print(type(answer))
                        #print(type(md5))
                        score+=1
                    else:
                        pass
                    i+=1
    
    print(score)