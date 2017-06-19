#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    currentA = headA
    currentB = headB
    same = True
    while currentA != None and currentB != None and same:
        if currentA.data != currentB.data:
            same = False
        else:
            currentA = currentA.next
            currentB = currentB.next
    if currentA == None and currentB == None and same:
        return 1
    else:
        return 0
