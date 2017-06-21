#!/bin/python

import sys

# Timing complexity is too high, need to reduce

class QueueNode:
    def __init__(self, value, steps):
        self.value = value
        self.steps = steps

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value, steps):
        temp = QueueNode(value, steps)
        self.queue.append(temp)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def length(self):
        return len(self.queue)

def factorsOf(n):
    return reduce(list.__add__, ([i] for i in range(1, int(n**0.5) + 1) if n % i == 0))

Q = int(raw_input().strip())
for a0 in xrange(Q):
    queue = Queue()
    N = int(raw_input().strip())
    queue.enqueue(N, 0)
    min_steps = sys.maxsize
    while queue.length() > 0:
        node = queue.dequeue()
        if node.value != 0 and node.steps < min_steps:
            factors = factorsOf(node.value)
            for i in xrange(1, len(factors)):
                queue.enqueue(max(factors[i], node.value/factors[i]), node.steps + 1)

            queue.enqueue(node.value - 1, node.steps + 1)

        else:
            if min_steps > node.steps:
                min_steps = node.steps
    print str(min_steps)
