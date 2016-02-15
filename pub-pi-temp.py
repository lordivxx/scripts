#!/usr/bin/python

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution. 
#
# The Eclipse Distribution License is available at 
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the publish.multiple helper function.

import sys

import subprocess

try:
    import paho.mqtt.publish as publish
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.publish"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.publish as publish


proc=subprocess.Popen('/home/pi/scripts/get-just-temp.sh', shell=True, stdout=subprocess.PIPE, )
pl=proc.communicate()[0]
pl=pl.strip()

#msgs = [{'topic':"paho/test/multiple", 'payload':pl}, ("paho/test/multiple", pl, 0, False)]


#publish.multiple(msgs, hostname="test.mosquitto.org")

publish.single("paho/test/pi-temp", pl, hostname="test.mosquitto.org")
