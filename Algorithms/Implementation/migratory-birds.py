#!/bin/python

import sys

def migratoryBirds(n, ar):
    birds = []
    for i in xrange(5):
        birds.append(0)

    for i in xrange(len(ar)):
        birds[ar[i]-1] += 1

    maxBirds = max(birds)
    return birds.index(maxBirds) + 1
    # Complete this function

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
