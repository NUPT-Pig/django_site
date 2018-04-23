#!/usr/bin/env bash
sudo apt-get install python3-pip -y
sudo apt-get install mysql-server -y
sudo apt-get install mysql-client -y
sudo apt-get install libmysqlclient-dev -y
sudo apt-get install apache2-dev -y
sudo apt-get install libapache2-mod-wsgi -y
sudo apt-get install redis-server -y


sudo pip3 install -r ~/PycharmProjects/django_site/configuration/requirements.txt