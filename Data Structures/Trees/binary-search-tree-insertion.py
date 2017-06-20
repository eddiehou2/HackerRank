"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""
import sys

def insert(r,val):
    temp = Node(val)
    if r == None:
        r = temp
    else:
        if val < r.data and r.left != None:
            insert(r.left, val)
        elif val < r.data and r.left == None:
            r.left = temp
        elif val >= r.data and r.right != None:
            insert(r.right, val)
        elif val >= r.data and r.right == None:
            r.right = temp
    return r
