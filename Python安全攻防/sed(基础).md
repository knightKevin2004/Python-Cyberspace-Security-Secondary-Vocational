# sed的用法

-e script 指定sed编辑命令

-f scriptfile 指定的文件中是sed编辑命令

-n 寂静模式，抑制来自sed命令执行过程中的冗余输出信息，比如只显示那些被改变的行。

-i[SUFFIX], –in-place[=SUFFIX] 替换和备份源文件

### 最基本的用法：

sed -i “s/被替换的内容/替换的内容/” 文件名（替换内容后的 “/” 是必须的）替换文件内容



### 例：

##### 参数“P”(打印指定行的内容)

sed -n "2p" /etc/passwd (打印/etc/passwd文件的第二行)

sed -n '1,3p' /etc/passwd（打印/etc/passwd文件的第一到第三行）

sed -n '/root/p' /etc/passwd（打印/etc/passwd文件中含有root的行）

sed -n '$p' /etc/passwd（打印/etc/passwd文件中的最后一行，”$“为最后一行）

##### 参数a和i: 插入文本和附加文本(插入新行)

sed -i '/asd/a\456' try.txt （在含有asd的行后添加一行，内容为“456”）

sed -i '/asd/i\123' try.txt（在含有asd的行前添加一行，内容为“123”）

sed -i '5 a\123' try.txt（在try.txt的第五行后添加一行，内容为“123”）

sed -i '5 i\123' try.txt（在try.txt的第五行前添加一行，内容为“123”）