# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solution():
    T = input()
    for i in xrange(T):
        N = input()
        colArray = map(int, sys.stdin.readline().strip().split(' '))
        colArray.sort()
        M = colArray[0]

        min_steps = sys.maxsize
        t = M
        while t > M - 5:
            steps = 0
            for i in xrange(len(colArray)):
                x = colArray[i] - t
                steps += x/5
                x %= 5
                steps += x/2
                x %= 2
                steps += x
            min_steps = min(steps, min_steps)
            t -= 1
        print str(min_steps)

solution()
    
