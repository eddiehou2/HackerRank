"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    head = None
    current = None
    currentA = headA
    currentB = headB
    while currentA != None and currentB != None:
        nextNode = None
        if currentA.data > currentB.data:
            nextNode = currentB
            currentB = currentB.next
        else:
            nextNode = currentA
            currentA = currentA.next

        if head == None:
            head = nextNode
            current = head
        else:
            current.next = nextNode
            current = current.next

    nextNode = None
    if currentA == None:
        nextNode = currentB
    elif currentB == None:
        nextNode = currentA
    if head == None:
        head = nextNode
        current = head
    else:
        current.next = nextNode
        current = current.next
    return head
