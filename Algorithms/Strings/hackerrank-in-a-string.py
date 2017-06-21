#!/bin/python

import sys


q = int(raw_input().strip())
hackerrank = "hackerrank"
for a0 in xrange(q):
    s = raw_input().strip()
    index = 0
    for i in xrange(len(s)):
        if index < len(hackerrank) and s[i] == hackerrank[index]:
            index += 1
    if index == len(hackerrank):
        print "YES"
    else:
        print "NO"
