#!/bin/bash

# Install github
sudo yum -y install github

# Download py installer
curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="/home/$USER/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Installrequirements packeges
sudo yum install -y libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel wget curl llvm ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config

# Install #.version
pyenv install 2.7.16
pyenv install 3.7.0

# Set as cuurent version
pyenv global 3.7.0

# Install pip && upgrade
sudo yum install -y python-pip
sudo pip install --upgrade pip

# Install virtualenv
sudo pip install virtualenv

# Create virtualenv environments
pyenv virtualenv 2.7.16 env1_2.7
pyenv virtualenv 3.7.0 env1_3.7

# Choose virtualenv environments
pyenv activate env1_3.7
