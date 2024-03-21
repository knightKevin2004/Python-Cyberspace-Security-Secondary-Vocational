def hanoi(n,A,B,C):
    if n==1:
        print(A,' ',C)
    else:
        hanoi(n-1,A,C,B)
        print(A,' ',C)
        hanoi(n-1,B,A,C)
hanoi(8,'A','B',"C")