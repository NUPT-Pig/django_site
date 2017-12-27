# redis安装启动相关
* 配置文件在/etc/redis/
* 启用Unix—sock,centos可以```chkconfig --level 2345 redis on```设置启动级别
* ```sudo redis-server /etc/redis/redis.conf``` (依据conf文件启动redis)
# redis远程连接
1. 注释掉 redis.conf 的 bind 127.0.0.1
2. ```sudo /etc/init.d/redis-server restart```
3. 远程主机 ```redis-cli -h redis主机ip -p 6379```
4. 程序中(*common_interface/redis_interface.py*)，将redis_interface里面host改成ip
# 备份操作
* django_site 修改了```redis.conf appendonly yes```
* aof 在 dir /var/lib/redis 里面