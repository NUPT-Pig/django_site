# django
# mysql
# django rest_framework
# redis
# libmysqlclient-dev
# apache2
# apache2-dev
# libapache2-mod-wsgi[-py3]
# django_site 下面创建log文件夹，当然也可以修改settings里面的日志目录
# 部署
+ wsgi + apache2 + ubuntu 部署
    - sudo apt-get install apache2 apache2-dev libapache2-mod-wsgi[-py3]
    - 新建 /etc/apache2/sites_available/django_site.conf
    - chmod -R 777 (需要写入log的文件)
    - django.wsgi.py 文件修改
    - a2ensite django_site

ps: /etc/apache2/ports.conf  可以修改监听的端口
/etc/apache2/apache2.conf 是总入口
里面没有Include available文件夹，所以需要手动a2ensite,
除非放在sites_enable文件夹下,当然a2ensite之后，也会放入enable文件夹下。
错误信息可在/var/log/apache2下查看
