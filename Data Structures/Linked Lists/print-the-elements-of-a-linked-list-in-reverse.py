"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def ReversePrint(head):
    arr = []
    current = head
    while current != None:
        arr.append(current.data)
        current = current.next
    for x in list(reversed(arr)):
        print str(x)
