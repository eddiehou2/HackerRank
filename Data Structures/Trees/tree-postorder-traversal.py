"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

def postOrder(root):
    if root == None:
        return

    postOrder(root.left)
    postOrder(root.right)
    sys.stdout.write(str(root.data) + " ")
