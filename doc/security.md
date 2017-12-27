# django(rest_frame)安全认证
* settings里面MIDDLEWARE AUTHENTICATION_BACKENDS 启用session
* REST_FRAMEWORK 决定认证是否通过(调式的时候改成AllowAny)
* login的处理view要在开头去掉认证,不然连login的request也会被拦截
    ```
    authentication_classes = ()
    permission_classes = ()
    ```
# 开启https
1. 首先开启 ssl 模块  ```sudo a2enmod ssl```
2. 生成自签名证书：
- 服务器私钥
    ```openssl genrsa -out server.key 1024```
- 服务器公钥
    ```openssl req -new -key server.key -out server.csr```
- 本来是把csr给ca机构，ca机构用它的私钥生成crt，给客户端的，客户端用ca的公钥验证crt是否来源可靠，
这里我们自生成。浏览器ca公钥验证不过，认为来源危险，会提醒是否要信任，信任就可以了,
然后客户端就从crt获取公钥了。客户端公钥加密，服务端私钥解密。
    ```openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt```
3. 拷贝到相应文件夹
    su 获取root权限
    ```
    cp server.crt /etc/ssl/certs/
    cp server.key /etc/ssl/private/
    ```
4. 修改/etc/apache2/sites_available/django_site.conf  启用ssl