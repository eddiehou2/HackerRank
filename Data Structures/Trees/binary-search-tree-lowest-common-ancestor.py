"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    if root == None:
        return root

    smaller = min(v1, v2)
    bigger = max(v1, v2)
    if root.data < smaller:
        return lca(root.right, v1, v2)
    elif root.data > bigger:
        return lca(root.left, v1, v2)
    else:
        return root
