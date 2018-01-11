# mysql客户端的安装与启动
1. ```sudo apt-get install libmysqlclient-dev```
2. 测试用的mysql 用户名root  密码root
3. 在mysql中创建新的数据库
```create database test```
4. 在 django.settings 里面配置mysql的连接
5. 将configuration里面的my.conf拷贝到 /etc/mysql/ 下（添加了中文支持）
# 远程连接
1. settings 设置 database 远程的 ip 和 port
2. 远程的mysql服务器*/etc/mysql/my.conf*注释掉```bind-address = 127.0.0.1```
- 2.1. 方法一：授予另外一个用户
```
    mysql
    use mysql
    GRANT ALL PRIVILEGES ON \*.\* TO 'remoteuser'@'%' IDENTIFIED BY 'remoteuser' WITH GRANT OPTION;
    FLUSH   PRIVILEGES;
```
修改settings里面的USER和PASSWORD为 remoteuser 和 remoteuser
- 2.2. 方法二：授予root权限
    ```mysql
    use mysql
    update user set host = '%' where user = 'root';  #  ignore error
    select host, user from user;  #  just a check
    flush privileges;
    ```
settings里面的USER和PASSWORD为root账户的用户名和密码 测试安装设置为 root和root
# mysql存储中文出错
* 报错信息：1267, "Illegal mix of collations (latin1_swedish_ci,IMPLICIT) and (utf8_general_ci,COERCIBLE) for operation '='"
* django 1.10 auth_user username python2 只可以 英文  python3 可以支持 Unicode 可修
* [参考文章](http://blog.csdn.net/wujingwen1111/article/details/12652819)
## 1查看字符编码方法小结
```
SHOW VARIABLES LIKE 'character_set_%';
```
|Variable_name|Value|
:-----|:-----|
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |

```
SHOW VARIABLES LIKE 'collation_%';
```
| Variable_name        | Value             |
|:-----|:-----|
| collation_connection | utf8_general_ci   |
| collation_database   | utf8_general_ci   |
| collation_server     | latin1_swedish_ci |
## 2修改编码方式
原因找到，原来是几项不是*utf8*编码，改成*utf8*编码即可：
```
set character_set_server =utf8;
SET collation_server = utf8_general_ci；
```
然而还是不可以，继续查看表里面的字段，可以发现表的字段编码没有改变：
```
show create table auth_user
```
改变username字段编码：
```
ALTER TABLE auth_user CHANGE username username VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci;
```
如此就可以了。

## 3避免出错方法
这只是修BUG，如何确保不出现这种情况，可以在配置mysql上就更改：
```
vi /etc/my.cnf

[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
default-character-set=utf8
```
然后重启数据库

当然还要确保客户端创建新的表和数据库也是使用utf8:
```
mysql --default-character-set=utf8 -u root -p
```
如果mysql的配置不能更改，那么就更改数据库，表和字段的编码：
```
ALTER DATABASE `test` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
ALTER TABLE `category` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
ALTER TABLE `test` CHANGE `dd` `dd` VARCHAR(45) CHARACTER SET utf8 COLLATE utf8_general_ci
```
