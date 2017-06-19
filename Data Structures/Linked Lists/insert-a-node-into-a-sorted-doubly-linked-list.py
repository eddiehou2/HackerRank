"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def SortedInsert(head, data):
    temp = Node(data)
    if head == None:
        head = temp
        return head

    current = head
    previous = None
    stop = False
    while current != None and not stop:
        if data > current.data:
            previous = current
            current = current.next
        else:
            stop = True

    if previous == None:
        temp.next = current
        current.prev = temp
        head = temp
    elif stop:
        previous.next = temp
        temp.prev = previous
        temp.next = current
        current.prev = temp
    else:
        previous.next = temp
        temp.prev = previous
    return head
