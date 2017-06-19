"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head == None:
        return head

    current = head.next
    previous = head
    while current != None:
        if current.data == previous.data:
            previous.next = current.next
        else:
            previous = current
        current = current.next

    return head
