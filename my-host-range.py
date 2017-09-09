#!/usr/bin/python

from IVXX_Tools import IVXX
import os


x = IVXX(os.environ["USER"])

host_range = x.get_user_input("Host Range: ")

x.run_bash_cmd("uptime")

