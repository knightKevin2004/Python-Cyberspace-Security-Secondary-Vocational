#因为这个程序是linux的所以在这里跑不出来,并且去linux里要给他附加执行权限
from pwn import *

T = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f']

a = 'actf{'
b = 0
pty = 1
while 1:
    if b == 12:
        break
    for i in T:
        io = process('C:\\Users\\Kevin\\Downloads\\SoulLike')      #这里括号里的内容要写自己电脑上SoulLike文件的下载位置！
        #启动本地程序进行交互，用于gdb调试
        flag = a + i
        flag = flag.ljust(17,'@')#返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
        flag += '}'
        success(flag)
        io.sendline(flag)       ## sendline发送数据会在最后多添加一个回车
        io.recvuntil('#')       #读取到指定数据
        if b < 9 :
            n = int(io.recv(1)) # recv(n)读取n个字节
        else:
            n = int(io.recv(2))
        io.close()              #关闭连接
        if n == b + 1:          #判断这一位是否正确 
            a = a + i
            b = b + 1
            break