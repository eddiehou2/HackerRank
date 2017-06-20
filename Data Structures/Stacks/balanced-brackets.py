#!/bin/python
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

opening = ["{", "[", "("]
closing = ["}", "]", ")"]
t = int(raw_input().strip())
for a0 in xrange(t):
    stack = Stack()
    s = raw_input().strip()
    balanced = True
    for c in s:
        if c in opening:
            stack.push(c)
        elif c in closing:
            match = ""
            if stack.length() > 0:
                match = stack.pop()
            if not(match in opening) or closing.index(c) != opening.index(match):
                balanced = False

    if balanced and stack.length() == 0:
        print "YES"
    else:
        print "NO"
