def prime(number):
    for c in range(2,number):
        if number%c==0:
            break
        
    else:
        print(str(number)+"是质数")
        return 0

def fenjie(number):
    
    for i in range(2,number+1):
        if number%i==0 and number!=i:
            zhishu.append(str(i))
            return fenjie(int(number/i))
        elif number==i:
            return zhishu.append(str(i))
    

if __name__=="__main__":
    zhishu=[]
    number=int(input('一个数'))
    if prime(number)!=0:
        fenjie(number)
        print(zhishu)