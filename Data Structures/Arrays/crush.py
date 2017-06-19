# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N, M = map(int,raw_input().strip().split(' '))
array = [0] * N
# Brute force approach does not work due to time complexity, instead adding to the start and subtracting at the element after the end has the same effects without time issues
for i in xrange(M):
    start, end, amount = map(int, raw_input().strip().split(' '))
    array[start-1] += amount
    if end < N:
        array[end] -= amount

max = 0
curAmount = 0
for i in xrange(N):
    curAmount += array[i]
    if (curAmount > max):
        max = curAmount
print max