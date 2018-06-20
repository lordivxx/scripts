#!/bin/bash -l


for x in `ls -d $HOME/repos/*`
	do 
		git --work-tree=$x --git-dir=$x/.git pull 
	done
