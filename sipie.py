#!/usr/bin/env python
# Eli Criffield

import os
import sys
from optparse import OptionParser
from Sipie import Interface

usage = "Usage: %prog [OPTIONS] [STATION]"
parser = OptionParser(usage=usage)
parser.add_option("-l", "--list", dest="list",
    action='store_true', default=False,
    help="list channels (Lots)")
parser.add_option("-s", "--setup", dest="setup",
    action='store_true', default=False,
    help="run setup")
parser.add_option("-q", "--quiet", dest="quiet",
    action='store_true', default=False,
    help="quiet the output to command line")

(opts, args) = parser.parse_args()

station = None
if len(args) > 0:
    station = args[0]
Interface(opts, station)
