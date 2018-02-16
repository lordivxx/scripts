#!/bin/bash -l

while true; do
	fnum=`squeue -u forsythc| wc -l`
	if [[ $fnum < 2 ]]; then
		break
	fi
	sleep 60
done
show-my-jobs.sh| wc -l | mail -s "jobs are done" forsythc@ucr.edu
