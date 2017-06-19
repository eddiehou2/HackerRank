#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    count = 0
    current = head
    while current != None:
        count += 1
        current = current.next

    index = count - position - 1
    count = 0
    current = head
    while current != None and index != count:
        count += 1
        current = current.next
    return current.data
