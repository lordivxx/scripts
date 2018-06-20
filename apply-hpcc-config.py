#! /usr/bin/python

####### Load modules ##########
import subprocess
from subprocess import Popen, PIPE
import time
import os
import sys
import argparse
import ConfigParser

########## Get location of users cfncluster config file   ###########
homepath = os.environ['HOME']
clusterconfigfile = homepath + "/.cfncluster/config"
#clusterconfigfile = "../configs/sample-base-config-test"


########## Main Code ##########
if __name__ == '__main__':

    ###### Initailize ConfigParser and read in config file
    Config = ConfigParser.ConfigParser()
    Config.read(clusterconfigfile)

    ###### Set Values for config file update
    Config.set('cluster default', 'compute_instance_type', 'c5.2xlarge')
    Config.set('cluster default', 'master_instance_type', 'c5.large')
    Config.set('cluster default', 'master_root_volume_size', '70')
    Config.set('cluster default', 'scheduler', 'slurm')
    Config.set('cluster default', 'initial_queue_size', '1')
    Config.set('cluster default', 'max_queue_size', '3')
    Config.set('cluster default', 'maintain_initial_size', 'true')
    Config.set('cluster default', 'post_install', 'http://biocluster.ucr.edu/~jhayes/aws/hpcc-bootstrap.sh')
    Config.set('cluster default', 'shared_dir', '/hpcc')
    Config.set('cluster default', 'ebs_settings', 'hpcc')
    Config.add_section('ebs hpcc')
    Config.set('ebs hpcc', 'volume_size', '100')
    Config.set('ebs hpcc', 'ebs_snapshot_id', 'snap-0fa4a9afa130ae3cb')
    Config.set('ebs hpcc', 'volume_type', 'gp2')

    ###### Write to config file adding and overwrite values
    with open(clusterconfigfile, 'w') as configfile:
        Config.write(configfile)

