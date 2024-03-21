n=int(input("输入一个数字"))
all=0.0
if n%2==0:
    for i in range(2,n+1,2):
        i=1/i
        all+=i
    print(all)
elif n%2==1:
    for i in range(2,n+1,2):
        i=1/i
        all+=i
    print(all)