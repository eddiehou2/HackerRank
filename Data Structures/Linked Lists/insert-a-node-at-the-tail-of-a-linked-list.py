"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""

def Insert(head, data):
    current = head
    previous = None
    temp = Node(data)
    while current != None:
        previous = current
        current = current.next
    if previous == None:
        head = temp
    else:
        previous.next = temp
    return head
