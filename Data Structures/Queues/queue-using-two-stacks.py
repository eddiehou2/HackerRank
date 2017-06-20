# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
# Did not need to use 2 stacks

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

N = input()
queue = Queue()
for i in xrange(N):
    command = map(int, sys.stdin.readline().strip().split(" "))
    if command[0] == 1:
        queue.enqueue(command[1])
    elif command[0] == 2:
        queue.dequeue()
    elif command[0] == 3:
        print queue.peek()
