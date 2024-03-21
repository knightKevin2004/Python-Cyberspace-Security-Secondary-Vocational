values = input("输入:")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))