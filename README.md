django_site
=======================================================
1.
----------------------------------------------------------
安装django, mysql, django rest_framework（记得加到settings的installed app）
redis(配置文件在/etc/redis/,启用Unix——sock,chkconfig --level 2345 redis on 设置启动级别)

2.
-------------------------------------------------------------
    django-admin startproject django_site

3.
------------------------------------------------------------------------------------
    sudo apt-get install libmysqlclient-dev
mysql 用户名root  密码root
在mysql中创建新的数据库  create database test, 并在 settings 里面配置mysql的连接

4.
------------------------------------------------------------------------------------------
    python manage.py startapp students
在settings里面installed_apps里面添加students

5.
-----------------------------------------------------------------------------------
创建数据模型后
    python manage.py makemigrations students
    python manage.py migrate
    
6.
----------------------------------------------------------------------------------
安全认证
settings里面MIDDLEWARE AUTHENTICATION_BACKENDS 启用session
REST_FRAMEWORK 这里面决定认证是否通过  调式的时候改成AllowAny
login的处理view要在开头去掉认证,不然连login的request也会被拦截
    
7.
-----------------------------------------------------------------------------
发布前必须 DEBUG = False 
    
8.
--------------------------------------------------------------------
log_interface里面的filename换掉
    
9.
------------------------------------------------------------------------------
    python manage.py run_all_supporters start<stop list restart>

10.
--------------------------------------------------------------------------------------
wsgi + apache2 + ubuntu 部署
    sudo apt-get install apache2-dev libapache2-mod-wsgi
新建 /etc/apache2/sites_available/django_site.conf
chmod -R 777 (需要写入log的文件)
wsgi.py 文件修改
    a2ensite django_site
ps: /etc/apache2/ports.conf  可以修改监听的端口 /etc/apache2/apache2.conf 是总入口，里面没有Include available文件夹，
>>所以需要手动a2ensite,除非放在sites_enable文件夹下,当然a2ensite之后，也会放入enable文件夹下。

11.
---------------------------------------------------------------------------------------------------------------
开启https
1. 首先开启 ssl 模块  sudo a2enmod ssl
2. 生成自签名证书：   
* 服务器私钥
    openssl genrsa -out server.key 1024
* 服务器公钥
    openssl req -new -key server.key -out server.csr
* 本来是把csr给ca机构，ca机构用它的私钥生成crt，给客户端的，客户端用ca的公钥验证crt是否来源可靠，这里我们自生成。浏览器ca公钥验证不过，认为来源危险，会提醒是否要信任，信任就可以了,然后客户端就从crt获取公钥了。客户端公钥加密，服务端私钥解密。
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
3. 拷贝到相应文件夹
    su 获取root权限
    cp server.crt /etc/ssl/certs/
    cp server.key /etc/ssl/private/
4. 修改django_site.conf  启用ssl
