#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

# Set max sum to most negative int, iterate through the array for all position middle of an hourglass and check for max sum
maxHourglassSum = -sys.maxsize-1
for row in xrange(1,5):
    for col in xrange(1,5):
        maxHourglassSum = max(sum(arr[row-1][col-1:col+2]) + arr[row][col] + sum(arr[row+1][col-1:col+2]), maxHourglassSum)

print maxHourglassSum
