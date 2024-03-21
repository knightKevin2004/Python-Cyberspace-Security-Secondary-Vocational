# coding:utf-8
while True:
    print('''
    *********欢迎使用货币转换服务*********
    1.人民币转换美元
    2.美元转换人民币
    3.人民币转换欧元
    0.结束程序
    '''
    )
    ch=input('请您选择需要的服务:')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if ch==str(1):
        print('欢迎使用人民币转美元服务')
        print('请输入需要转换的人民币金额')
        num=float(input())
        print('你需要转换的人民币为:'+str(num))
        print('兑换成美元为:%.2f'%(num/7.06))
    elif ch==str(0):
        print('感谢你的使用,祝您生活愉快,再见!')
        break
    else:
        print('输入错误')