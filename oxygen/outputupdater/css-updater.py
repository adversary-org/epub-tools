#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

import datetime
import time
import os
import os.path
import sys

ct = time.ctime
ddt = datetime.datetime
dd = datetime.datetime.date
dt = datetime.datetime.time
ls = os.listdir
op = os.path
ow = os.walk

# Get rid of what's not needed when done.
#
# assume this is to be run from anywhere, but takes the project directory (or
# directory where the main map file is) as the sole input, even as a relative
# path.  Will probably end up with slightly customised ones for particular
# projects.
#
# Default config will be to make a custom build folder in th each project and
# place this in there (instead of XSL bollocks or alternate ant scripts).  Then
# everything is relative to the script, including source data and output.
#
# Developing and testing initiated with the soon-to-be-published "Project 77"
# (working title).
