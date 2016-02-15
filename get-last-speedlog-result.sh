#!/bin/bash

tail -1 /home/pi/speedtest/speedtest.log | awk -F ";" '{print $8}'| awk '{print $1}'
