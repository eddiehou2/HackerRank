# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N = int(sys.stdin.readline())
arr = []
for i in xrange(N):
    arr.append(sys.stdin.readline().strip())
Q = int(sys.stdin.readline())
for i in xrange(Q):
    count = 0
    query = sys.stdin.readline().strip()
    for j in xrange(len(arr)):
        if (arr[j] == query):
            count += 1
    print count
