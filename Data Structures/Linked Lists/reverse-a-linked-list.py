"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    previous = None
    current = head
    if head == None:
        return head
    nextNode = head.next
    while nextNode != None:
        current.next = previous
        previous = current
        current = nextNode
        nextNode = nextNode.next
    current.next = previous
    return current
