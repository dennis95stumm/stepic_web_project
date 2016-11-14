#!/bin/bash

sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo rm -rf /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepik CHARACTER SET utf8;"
mysql -u root -e "CREATE USER 'stepik'@'localhost' IDENTIFIED BY 'stepik';"
mysql -u root -e "GRANT ALL ON stepik.* TO 'stepik'@'localhost';"
