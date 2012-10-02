#!/usr/bin/env python

import sys
import re

def getpie(argv):
    for line in sys.stdin:
        # remove extraneous white space
        clean_line = line.strip()
        # split into fields
        pieces = clean_line.split("\t")
        ngram = pieces[0].lower()
        if re.search("pie",ngram):
            print "LongValueSum:" + ngram + "\t" + "1"

if __name__ == "__main__":
     getpie(sys.argv)
