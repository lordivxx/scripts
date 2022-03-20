#!/bin/bash -l


pip install gdown

gdown --fuzzy https://drive.google.com/file/d/1QdYbTArQFVSeg1WF4xm95nO5wiAO4LX1/view?usp=sharing

chmod 755 install-vhpc.sh

./install-vhpc.sh 2> e.logz 1> o.logz
