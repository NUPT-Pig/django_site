mysql存储中文出错：1267, "Illegal mix of collations (latin1_swedish_ci,IMPLICIT) and (utf8_general_ci,COERCIBLE) for operation '='"
参考：http://blog.csdn.net/wujingwen1111/article/details/12652819
SHOW VARIABLES LIKE 'character_set_%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+

SHOW VARIABLES LIKE 'collation_%';
+----------------------+-------------------+
| Variable_name        | Value             |
+----------------------+-------------------+
| collation_connection | utf8_general_ci   |
| collation_database   | utf8_general_ci   |
| collation_server     | latin1_swedish_ci |
+----------------------+-------------------+

原因找到，原来是几项不是utf8编码，改成utf8编码即可：
set character_set_server =utf8;
SET collation_server = utf8_general_ci；

然而还是不可以，继续查看表里面的字段，可以发现表的字段编码没有改变：
show create table auth_user

改变username字段编码：
ALTER TABLE auth_user CHANGE username username VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci;

如此就可以了。


这只是修BUG，如何确保不出现这种情况，可以在配置mysql上就更改：
vi /etc/my.cnf

[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
default-character-set=utf8

然后重启数据库

当然还要确保客户端创建新的表和数据库也是使用utf8,
mysql --default-character-set=utf8 -u root -p

如果mysql的配置不能更改，那么就更改数据库，表和字段的编码：

ALTER DATABASE `test` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
ALTER TABLE `category` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
ALTER TABLE `test` CHANGE `dd` `dd` VARCHAR( 45 ) CHARACTER SET utf8 COLLATE utf8_general_ci

