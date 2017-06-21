# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Already optimized but not fast enough to pass 20,21,22,23

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

    def percDown(self, i):
        stop = False
        while (i*2) <= self.currentSize and not stop:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = temp
                i = mc
            else:
                stop = True

    def minChild(self, i):
        if (i*2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i*2] > self.heap[i*2 + 1]:
                return i*2 +1
            else:
                return i*2

    def popMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.heap.pop()
        self.currentSize -= 1
        self.percDown(1)
        return retval

    def peekMin(self):
        return self.heap[1]

    def mixCookies(self):
        s1 = self.popMin()
        self.heap[1] = s1 + 2 * self.heap[1]
        self.percDown(1)


N, K = map(int, sys.stdin.readline().strip().split(" "))
A = map(int, sys.stdin.readline().strip().split(" "))
heap = BinHeap()
for i in xrange(len(A)):
    heap.insert(A[i])

if heap.currentSize != 0:
    s1 = 0
    s2 = 0
    impossible = False
    total_steps = 0
    while heap.peekMin() < K and not impossible:
        if heap.currentSize > 1:
            heap.mixCookies()
            total_steps += 1
        elif heap.currentSize == 1:
            print "-1"
            impossible = True
    if not impossible:
        print total_steps
