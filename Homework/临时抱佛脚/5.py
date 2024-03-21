str_list=[]
num=0
string="When your mind is simple,your world is simple"
for x in string:
    str_list.append(x)
    num+=1
    if x==str('r'):
        r=num
    elif x==str('a'):
        a=num
    else:
        none="-1"

print("获取元素i的个数:"+str(str_list.count("i")))
print("判断开头的元素是不是e:"+str(bool(str_list[0]=="e")))
print("判断结尾的元素是不是e:"+str(bool(str_list[-1]=="e")))
print("请找到元素r在哪个位置:"+str(r))
print("请找到元素a在哪个位置:"+str(none))
print("请把字符串中的元素W去掉:")
print("请把字符中的your改成my:")
print("请判断字符串是不是由空格组成:")
print("请判断字符串是不是标题:")
print("请判断字符串中的字母是不是都是大写:")
print("请判断字符串中的字母是不是都是小写:")