#!/bin/bash -l


case "$1" in
  status)

for x in `ls -d $HOME/repos/*`
        do
                cd $x; echo $x; git status
        done
        ;;
       *)

for x in `ls -d $HOME/repos/*`
        do
                echo $x; git --work-tree=$x --git-dir=$x/.git pull
        done

esac

