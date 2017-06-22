# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = input()
ar = map(int, sys.stdin.readline().strip().split(" "))
countArray = [0] * 100
for i in xrange(n):
    countArray[ar[i]] += 1

temp = []
for i in xrange(100):
    temp += countArray[i] * [i]

print " ".join(map(str, temp))
