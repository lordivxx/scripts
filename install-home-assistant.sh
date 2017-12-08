#!/bin/bash

yum install -y python-virtualenv python3
#rm -rf $HOME/virtualenvs/home-assistant
virtualenv --system-site-packages -p python3 /home/forsythc/virtualenvs/home-asssistant
#source /home/forsythc/virtualenvs/home-asssistant/bin/activate
/$HOME/virtualenvs/home-asssistant/bin/pip3 install homeassistant
#~/virtualenvs/home-asssistant/bin/python3 /home/forsythc/virtualenvs/home-asssistant/bin/hass --open-ui
