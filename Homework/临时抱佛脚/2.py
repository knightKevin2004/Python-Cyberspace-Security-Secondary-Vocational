'''
def main(x):
    y=1
    for x in range(1,x+1):
        y=x*y
    print(y)
x=int(input("乘到多少"))
main(x)
'''


def digui(x):
    if x ==1:
        return 1
    else:
        return x * digui(x-1)
a=int(input('请输入一个数'))
b=digui(a)
print(b)