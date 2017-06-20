import sys

# Implemented max stack nodes to get O(1) time complexity
class StackNode:
    def __init__(self, val, cur_max, above_max):
        self.value = val
        self.cur_max = cur_max
        self.above_max = above_max

stackArray = []
N = input()
cur_max = -sys.maxsize-1
above_max = 0
for i in xrange(N):
    command = map(int, sys.stdin.readline().strip().split(' '))
    if command[0] == 1:
        if cur_max < command[1]:
            cur_max = command[1]
            above_max = 0
        else:
            above_max += 1
        stackNode = StackNode(command[1], cur_max, above_max)
        stackArray.append(stackNode)
    elif command[0] == 2:
        removed = stackArray.pop()
        if removed.above_max == 0 and len(stackArray) != 0:
            cur_max = stackArray[len(stackArray)-1].cur_max
            above_max = stackArray[len(stackArray)-1].above_max
        elif len(stackArray) == 0:
            cur_max = -sys.maxsize-1
            above_max = 0
        else:
            above_max -= 1
    elif command[0] == 3:
        print str(cur_max)
