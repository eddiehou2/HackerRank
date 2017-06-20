"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

def levelOrder(root):
    if root == None:
        return

    arr = [root]
    current = arr[0]
    index = 0
    while current != None and index < len(arr):
        current = arr[index]
        if current.left != None:
            arr.append(current.left)
        if current.right != None:
            arr.append(current.right)
        sys.stdout.write(str(current.data) + " ")
        index += 1
