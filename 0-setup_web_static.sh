#!/usr/bin/env bash
#script for creating files for web

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo sed -i "42i\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enabled/default
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo service nginx restart
