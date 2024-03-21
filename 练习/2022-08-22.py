def prime(s,e):
    count=0
    for i in range(s,e,2):
        for c in range(2,int(i**0.5)+1):
            if i%c==0:
                flag=0
                break
        if flag:
            print('{:>{}}'.format(i,len(str(e))),end=' ')
            count+=1
            if count==10:
                print()
                count=0
        else:
            flag=1

if __name__=='__main__':
    prime(99,1001)
    print()