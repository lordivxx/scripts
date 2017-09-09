#!/usr/bin/python

from IVXX_Tools import IVXX
import os

# Initailize the IVXX Tools Kit and the current user
x = IVXX(os.environ["USER"])

#Build OS command to run
cmd = "sinfo -n i[10-20] -o \"%n %c %m %O %e %C %T\""

# Fire off the command
x.run_bash_cmd(cmd)



