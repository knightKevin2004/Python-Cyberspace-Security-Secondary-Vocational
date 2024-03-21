a=r"20f0Th{2tsIS_icArE}e7__w"
b=r"2f0t02T{hcsiI_SwA__r7Ee}"
root=end=len(a)
start=0
def f(root,start,end):
    if start>end:
        pass
    i=start
    while i<end and b[i]!=a[root-1]:
        i+=1
    print("%c"%(b[i]))
    f(root-1-(end-i),start,i-1)
    f(root-1,i+1,end)
def main():
    f(root,start,end)
    return 0
main()