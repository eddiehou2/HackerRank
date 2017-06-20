"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""
import sys

def topView(root):
  #Write your code here
    if root == None:
        return

    topViewHelper(root.left, True)
    sys.stdout.write(str(root.data) + " ")
    topViewHelper(root.right, False)

def topViewHelper(root, left):
    if root == None:
        return

    if left:
        topViewHelper(root.left, left)
        sys.stdout.write(str(root.data) + " ")
    else:
        sys.stdout.write(str(root.data) + " ")
        topViewHelper(root.right, left)
    
