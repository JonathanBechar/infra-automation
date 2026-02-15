#!/bin/bash
#
# The script checks if nginx is installed, if not, installs and enables it.
#
set -e
if dpkg -s nginx &>/dev/null
then
    echo "Nginx already installed"
sudo apt install nginx 
else
    echo "Installing nginx..."
    sudo apt update
    sudo apt install nginx
fi

echo "Starting nginx..."
systemctl start nginx
echo "Enabling nginx at boot..."
systemctl enable nginx
echo "Finished"
