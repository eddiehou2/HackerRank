#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
arr.sort()
print str(sum(arr[:-1])) + " " + str(sum(arr[1:]))
