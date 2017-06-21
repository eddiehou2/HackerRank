#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    ar.sort()
    count = 0
    tallest = ar[n-1]
    i = n-1
    while i >= 0 and tallest == ar[i]:
        count += 1
        i -= 1
    return count


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
