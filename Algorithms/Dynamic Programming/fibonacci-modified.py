# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

t1, t2, n = map(int, sys.stdin.readline().strip().split(" "))
if n == 0:
    print -1
elif n == 1:
    print t1
elif n == 2:
    print t2

t = [0,t1,t2]
for i in xrange(3, n+1):
    t.append(t[i-2]+(t[i-1]*t[i-1]))

print t[len(t)-1]
