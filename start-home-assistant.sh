#!/bin/bash


kill `ps aux | grep hass | grep -v grep | awk '{print $2}'`
nohup $HOME/virtualenvs/home-asssistant/bin/python3 $HOME/virtualenvs/home-asssistant/bin/hass --open-ui  
