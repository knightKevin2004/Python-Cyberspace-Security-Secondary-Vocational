# mysql修改密码及无密码登录

## 已知密码

### 1.使用mysqladmin修改密码

```
mysqadmin -u root -p password newpassword
```

### 2.进入mysql更改密码

```
set password for root@'%'=password("newpasswd");
```

### 3.手动改表更改密码

```
update mysql.user set passowrd=password("newpasswd") where user='root';
```

#### 4.grant更改

```
grant all privileges on *.* to 'root'@"%" identified by "newpasswd" with grant option
```

## 未知密码直接登录

### linux

```
添加skip-grant-tables至配置文件
重启服务
mysql -uroot -h192.168.1.1 -p
```

### widnows

```
查看mysql进程端口3306
netstat -ano
taskkill /pid 1224 /F
mysqld.exe --skip-grant-tables
mysql -uroot -p192.168.1.1 -p
```