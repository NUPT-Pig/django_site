# rest_framework 安装
* 记得加到settings的installed app
# django 工程建立
1. ```django-admin startproject project_name```
2. ```python manage.py startapp app_name```
3. 在settings->installed_apps->添加app
# 创建model后数据库同步
*   ```
    python manage.py makemigrations students
    python manage.py migrate
    ```
# 定制middle_ware
* django 的 middleware 可以全局modify request 和 response
* rest_framework 的 middleware 可以全局检测 permission 和 authentication,但是不能控制request和response。
  它的好处是，可以在每个views里面控制authentication的检测目标，例子可以看login的view。
* 定制middle_ware可以参考common_interface.restframework_middleware_interface.py