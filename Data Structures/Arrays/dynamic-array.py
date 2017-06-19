# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

NQ = sys.stdin.readline().split(' ')
N = int(NQ[0])
Q = int(NQ[1])
arr = []
lastAnswer = 0
for n in xrange(0,int(NQ[0])):
    arr.append([])
for q in xrange(0,int(NQ[1])):
    command, x, y = sys.stdin.readline().split(' ')
    seq = (int(x)^lastAnswer)%N
    if command == "1":
        arr[seq].append(int(y))
    else:
        lastAnswer = arr[seq][int(y)%len(arr[seq])]
        print lastAnswer

    
