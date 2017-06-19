#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
# Reversed iterator into a list and then join and for iteration to print out
print ' '.join(str(x) for x in list(reversed(arr)))
