# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class QueueNode:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x, y, steps):
        temp = QueueNode(x, y, steps)
        self.queue.append(temp)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def length(self):
        return len(self.queue)

N = input()
gridInput = []
for i in xrange(N):
    gridInput.append(sys.stdin.readline())

grid = []
visited = []
for i in xrange(N):
    grid.append([])
    visited.append([])
    for j in xrange(N):
        if gridInput[i][j] == ".":
            grid[i].append(True)
            visited[i].append(False)
        elif gridInput[i][j] == "X":
            grid[i].append(False)
            visited[i].append(True)


a, b, c, d = map(int, sys.stdin.readline().strip().split(" "))
queue = Queue()
queue.enqueue(a, b, 0)
visited[a][b] = True
while queue.length > 0:
    node = queue.dequeue()
    for x in xrange(1, N - node.x):
        if not grid[node.x + x][node.y]:
            break
        if not visited[node.x + x][node.y] and grid[node.x + x][node.y]:
            queue.enqueue(node.x + x, node.y, node.steps + 1)
            visited[node.x + x][node.y] = True
    for x in xrange(1, node.x + 1):
        if not grid[node.x - x][node.y]:
            break
        if not visited[node.x - x][node.y] and grid[node.x - x][node.y]:
            queue.enqueue(node.x - x, node.y, node.steps + 1)
            visited[node.x - x][node.y] = True
    for y in xrange(1, N - node.y):
        if not grid[node.x][node.y + y]:
            break
        if not visited[node.x][node.y + y] and grid[node.x][node.y + y]:
            queue.enqueue(node.x, node.y + y, node.steps + 1)
            visited[node.x][node.y + y] = True
    for y in xrange(1, node.y + 1):
        if not grid[node.x][node.y - y]:
            break
        if not visited[node.x][node.y - y] and grid[node.x][node.y - y]:
            queue.enqueue(node.x, node.y - y, node.steps + 1)
            visited[node.x][node.y - y] = True

    if node.x == c and node.y == d:
        print str(node.steps)
        break

    
