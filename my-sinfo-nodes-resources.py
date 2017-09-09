#!/usr/bin/python

from IVXX_Tools import IVXX
import os

# Initailize the IVXX Tools Kit and the current user
x = IVXX(os.environ["USER"])

cmdlvarinput = x.build_positional_argparse("input")
if cmdlvarinput == "check_string_for_empty":
    cmdlvarinput = "i[01-40],c[01-48],h[01-05],gpu[01-04]"

#Build OS command to run
cmd = "sinfo -n " + cmdlvarinput +" -o \"%n %c %m %O %e %C %T\""

# Fire off the command
x.run_bash_cmd(cmd)



