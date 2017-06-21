#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

pdSum = 0
sdSum = 0
for i in xrange(n):
    pdSum += a[i][i]
    sdSum += a[i][n-1-i]

print abs(pdSum - sdSum)
