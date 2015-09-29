#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  GPLv3
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "GPLv3"
__version__ = "0.0.1"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"

import datetime
import re
import sys

ddt = datetime.datetime
filename = "content.opf"
# newfile = "newcontent.opf"
utc = datetime.datetime.utcnow().isoformat()[:19]

pattern = '        <meta property="dcterms:modified">'
logrus = '        <meta property="dcterms:modified">{0}Z</meta>\n'.format(utc)

f = open(filename, "r")
lines = f.readlines()
f.close()

for line in lines:
    if line.startswith(pattern) is True:
        point = lines.index(line)
        # print(line)
        # print(lines[point])
        lines.remove(line)
        lines.insert(point, logrus)
        # print(lines[point])
    else:
        pass

# nf = open(newfile, "w")
# for line in lines:
#     nf.write(line)
# nf.close()

f = open(filename, "w")
for line in lines:
    f.write(line)
f.close()


