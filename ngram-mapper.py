#!/usr/bin/env python

import sys

for line in sys.stdin:
    ngram, year, cnt, pgs, bks = line.strip().split("\t")
    words = ngram.split(" ")
    if "bird" in words:
        print '%s\t%s\t%s' % (ngram, year, cnt)
