#!/bin/bash

weatherpy -o | awk '{ print $5 }'| head -4 | tail -1
#weatherpy | head -2 | tail -1 | awk '{ print $2 }'
