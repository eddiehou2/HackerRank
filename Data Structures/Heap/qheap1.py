# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Timing complexity failed on case 8 and 9

class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    def insert(self, value):
        self.heap.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        stop = False
        while i//2 > 0 and not stop:
            if self.heap[i] < self.heap[i//2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = temp
                i = i//2
            else:
                stop = True

    def minChild(self, i):
        if (i*2) + 1 > self.currentSize:
            return i*2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i*2+1
            else:
                return i*2

    def percDown(self, i):
        stop = False
        while i*2 <= self.currentSize and not stop:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = temp
                i = mc
            else:
                stop = True

    def popMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.percDown()
        return retval

    def deleteValue(self, value):
        index = self.indexMatchValue(value, 1)
        self.heap[index] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        if index <= self.currentSize:
            self.percDown(index)
            self.percUp(index)

    def indexMatchValue(self, value, i):
        if i > 0 and i <= self.currentSize:
            if self.heap[i] == value:
                return i
            else:
                return max(self.indexMatchValue(value, i*2), self.indexMatchValue(value, i*2+1))
        else:
            return -1

    def peekMin(self):
        return self.heap[1]

Q = input()
heap = BinHeap()
for i in xrange(Q):
    command = map(int, sys.stdin.readline().strip().split(" "))
    if command[0] == 1:
        heap.insert(command[1])
    elif command[0] == 2:
        heap.deleteValue(command[1])
    elif command[0] == 3:
        print str(heap.peekMin())
