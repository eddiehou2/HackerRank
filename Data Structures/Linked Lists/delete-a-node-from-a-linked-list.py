"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    current = head
    previous = None
    for i in xrange(position):
        previous = current
        current = current.next
    if previous == None:
        head = head.next
    else:
        previous.next = current.next
    return head
