# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def maxArea(h):
    if len(h) == 0:
        return 0

    smallest = min(h)
    area = smallest*len(h)
    index = h.index(smallest)
    if index < len(h) - 1:
        return max(area, maxArea(h[:index]), maxArea(h[index+1:]))
    else:
        return max(area, maxArea(h[:index]))


N = int(raw_input().strip())
h = map(int, sys.stdin.readline().strip().split(" "))
print maxArea(h)
