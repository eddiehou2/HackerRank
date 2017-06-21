#!/bin/python

import sys

def getRecord(s):
    highest = s[0]
    lowest = s[0]
    hb = 0
    lb = 0
    for i in xrange(1, len(s)):
        if highest < s[i]:
            highest = s[i]
            hb += 1
        if lowest > s[i]:
            lowest = s[i]
            lb += 1

    return [hb, lb]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
