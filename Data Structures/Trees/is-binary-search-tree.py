""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root == None:
        return True

    return left(root.left, root.data) and right(root.right, root.data)

def left(root, pdata):
    if root == None:
        return True

    if root.data >= pdata:
        return False
    return left(root.left, pdata) and left(root.left, root.data) and right(root.right, root.data) and left(root.right, pdata)

def right(root, pdata):
    if root == None:
        return True

    if root.data <= pdata:
        return False
    return right(root.left, pdata) and left(root.left, root.data) and right(root.right, root.data) and right(root.right, pdata)
