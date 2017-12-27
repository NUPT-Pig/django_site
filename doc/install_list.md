# django
# mysql
# django rest_framework
# redis
# libmysqlclient-dev
# apache2-dev
# libapache2-mod-wsgi
# 部署
+ wsgi + apache2 + ubuntu 部署
    - sudo apt-get install apache2-dev libapache2-mod-wsgi
    - 新建 /etc/apache2/sites_available/django_site.conf
    - chmod -R 777 (需要写入log的文件)
    - django.wsgi.py 文件修改
    - a2ensite django_site

ps: /etc/apache2/ports.conf  可以修改监听的端口
/etc/apache2/apache2.conf 是总入口
里面没有Include available文件夹，所以需要手动a2ensite,
除非放在sites_enable文件夹下,当然a2ensite之后，也会放入enable文件夹下。
