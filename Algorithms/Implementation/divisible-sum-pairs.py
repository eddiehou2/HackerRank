#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    ways = 0
    for i in xrange(len(ar)-1):
        for j in xrange(i+1,len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                ways += 1

    return ways

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
