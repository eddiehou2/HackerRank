"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

def preOrder(root):
    if root == None:
        return

    sys.stdout.write(str(root.data) + " ")
    preOrder(root.left)
    preOrder(root.right)
