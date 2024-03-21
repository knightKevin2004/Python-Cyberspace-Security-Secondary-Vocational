# coding: utf-8

height = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
print('小明的身高是%s体重为%s'%(height,weight))

BMI=weight/height**2

if BMI<18.5:
    print("偏轻")
elif 18.5<=BMI<=25:
    print("正常")
elif 25<BMI<=28:
    print("过重")
elif 28<BMI<=32:
    print('肥胖')
else:
    print('严重肥胖')