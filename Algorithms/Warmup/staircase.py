#!/bin/python

import sys


n = int(raw_input().strip())



for i in xrange(n):
    out = [" "] * (n-1-i) + ["#"] * (i+1)
    sys.stdout.write("".join(out) + "\n")
        
