#!/bin/python
import sys

class StackNode:
    def __init__(self, value, height):
        self.value = value
        self.height = height

class Stack:
    def __init__(self):
        self.stack = []
        self.cur_height = 0

    def push(self, value):
        self.cur_height += value
        temp = StackNode(value, self.cur_height)
        self.stack.append(temp)

    def pop(self):
        temp = self.stack.pop()
        self.cur_height -= temp.value
        return temp

    def height(self):
        return self.cur_height

    def length(self):
        return len(self.stack)

def equilizer(s1, s2, s3):
    while not (s1.height() == s2.height() == s3.height()):
        if s1.height() >= s2.height() and s1.height() >= s3.height() and s1.length() > 0:
            s1.pop()
        elif s2.height() >= s1.height() and s2.height() >= s3.height() and s2.length() > 0:
            s2.pop()
        elif s3.height() >= s2.height() and s3.height() >= s1.height() and s3.length() > 0:
            s3.pop()
    print s1.height()

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
s1 = Stack()
s2 = Stack()
s3 = Stack()
for h in list(reversed(h1)):
    s1.push(h)
for h in list(reversed(h2)):
    s2.push(h)
for h in list(reversed(h3)):
    s3.push(h)

equilizer(s1, s2, s3)
