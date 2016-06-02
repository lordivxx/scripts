#!/bin/bash

echo "*********** Begin IO Stat ************"

/bin/sh -c "iostat 1 3 | tail -7"
echo ""
echo "*********** Begin Free Mem ***********"
echo ""
free -m
echo ""
echo "*********** Begin DF ***********"
echo ""
df -h
echo ""
echo "*********** Begin Netstat ***********"
echo ""
netstat -at
echo ""
echo "*********** Begin SAR ***********"
echo ""
sar -n TCP
echo ""
echo ""
echo "**********************"
