i = 0
j = 1
x = 0
while (i < 5) :
    print("i: %d\tj: %d\tx: %d"%(i,j,x))
    x = 4 * j
    for i in range(0,5) :
        print("x: %d\ti: %d"%(x,i))
        if(x%4 != 0) :
            print("break")
            break
        else :
            i += 1
            print("i: %d"%(i,))
        x = (x/4) * 5 +1
    j += 1
print(x)