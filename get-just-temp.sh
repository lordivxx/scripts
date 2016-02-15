#!/bin/bash

weatherpy -o | awk '{ print $5 }'| head -4 | tail -1
