#!/bin/python

import sys

def getTotalX(a, b):
    aMax = max(a)
    bMin = min(b)
    i = aMax
    between = True
    btArr = []
    factor = 2
    while i <= bMin:
        between = True
        for j in xrange(len(a)):
            if i % a[j] != 0:
                between = False
                break

        if between:
            for j in xrange(len(b)):
                if b[j] % i != 0:
                    between = False
                    break

        if between:
            btArr.append(i)

        i = aMax * factor
        factor += 1

    return len(btArr)



n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
