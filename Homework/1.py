x = int(input("此次的学习成绩为"))
if x >= 85 and x <=100:
    print("你的成绩是优秀")
elif x >= 60 and x < 85:
    print("你的成绩是良好")
elif x > 50 and x < 60:
    print("你不及格")
elif x <= 50:
    print("你需要补考")
else:
    print("你的数字有问题!")