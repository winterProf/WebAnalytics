#!/usr/bin/env python

import sys

for line in sys.stdin:
    cols = line.strip().split("\t")
    words = cols[0].split(" ")
    if "pie" in words and len(cols>2):
        print '%s\t%s\t%s' % (cols[0], cols[1], cols[2])
