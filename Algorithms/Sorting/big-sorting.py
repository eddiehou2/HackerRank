#!/bin/python

import sys

# Using a comparator would yield faster results

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = int(raw_input().strip())
    unsorted.append(unsorted_t)

unsorted.sort()
for x in xrange(len(unsorted)):
    print str(unsorted[x])
