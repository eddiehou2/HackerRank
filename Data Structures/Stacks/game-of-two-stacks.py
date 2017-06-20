#!/bin/python

import sys

# Fills to x with only items from A and then slowly replace each with items from B and get max score
g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    aSum = 0
    bSum = 0
    gottenA = []
    gottenB = []
    i = 0
    full = False
    while not full and i < len(a):
        if (aSum + a[i] <= x):
            aSum += a[i]
            gottenA.append(a[i])
        else:
            full = True
        i += 1

    i = len(gottenA)
    j = 0
    full = True
    max_score = i
    emptyA = False
    while not emptyA and full:
        cur_Sum = aSum + bSum
        full = False
        while not full and j < len(b):
            if (cur_Sum + b[j] <= x):
                cur_Sum += b[j]
                bSum += b[j]
                gottenB.append(b[j])
                j += 1
            else:
                full = True
        score = len(gottenA) + len(gottenB)
        max_score = max(score, max_score)

        if len(gottenA) > 0:
            dropped = gottenA.pop()
            aSum -= dropped
        else:
            emptyA = True

    print str(max_score)
