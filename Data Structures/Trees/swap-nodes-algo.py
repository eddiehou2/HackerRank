# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
class TreeNode:
    def __init__(self, initData):
        self.data = initData
        self.left = None
        self.right = None
        self.depth = 1



numOfNodes = int(sys.stdin.readline().strip())
nodeArr = [None] * numOfNodes
newNode = TreeNode(1)
nodeArr[0] = newNode
for i in xrange(1,numOfNodes+1):
    left, right = map(int, sys.stdin.readline().strip().split(" "))
    parentNode = nodeArr[i-1]
    if left != -1:
        newLeftNode = TreeNode(left)
        parentNode.left = newLeftNode
        newLeftNode.depth = parentNode.depth + 1
        nodeArr[left-1] = newLeftNode
    if right != -1:
        newRightNode = TreeNode(right)
        nodeArr[i-1].right = newRightNode
        newRightNode.depth = parentNode.depth + 1
        nodeArr[right-1] = newRightNode

root = nodeArr[0]
stackArr = []
T = int(sys.stdin.readline().strip())
for i in xrange(T):
    K = int(sys.stdin.readline().strip())
    for i in xrange(len(nodeArr)):
        if nodeArr[i].depth % K == 0:
            temp = nodeArr[i].left
            nodeArr[i].left = nodeArr[i].right
            nodeArr[i].right = temp
    current = root
    pop = False
    while current != None:
        if current.left != None and not pop:
            stackArr.append(current)
            current = current.left
        elif current.right != None:
            sys.stdout.write(str(current.data) + " ")
            current = current.right
            pop = False
        else:
            sys.stdout.write(str(current.data) + " ")
            if len(stackArr) > 0:
                current = stackArr.pop()
                pop = True
            else:
                current = None
    sys.stdout.write("\n")
