#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

appleCount = 0
for i in xrange(len(apple)):
    if apple[i] + a >= s and apple[i] + a <= t:
        appleCount += 1

orangeCount = 0
for i in xrange(len(orange)):
    if orange[i] + b >= s and orange[i] + b <= t:
        orangeCount += 1

print str(appleCount)
print str(orangeCount)
