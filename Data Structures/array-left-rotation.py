# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

nd = sys.stdin.readline().split(' ')
n = int(nd[0])
d = int(nd[1])

arr = sys.stdin.readline().split(' ')
arr = arr[d:]+arr[:d]
print " ".join(str(x) for x in arr)
