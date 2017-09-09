#!/usr/bin/python

from IVXX_Tools import IVXX
import os


x = IVXX(os.environ["USER"])

x.run_bash_cmd("uptime")

