# django_site

1.
    安装django, mysql, django rest_framework（记得加到settings的installed app）

2.
    django-admin startproject django_site

3.
    mysql 用户名root  密码root
    在mysql中创建新的数据库  create database test, 并在 settings 里面配置mysql的连接

4.
    python manage.py startapp students
    在settings里面installed_apps里面添加students

5.
    创建数据模型后
    python manage.py makemigrations students
    python manage.py migrate
    
6.
    安全认证
    settings里面MIDDLEWARE AUTHENTICATION_BACKENDS 启用session
    REST_FRAMEWORK 这里面决定认证是否通过  调式的时候改成AllowAny