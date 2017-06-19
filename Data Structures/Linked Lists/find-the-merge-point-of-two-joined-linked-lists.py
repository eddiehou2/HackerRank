"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def FindMergeNode(headA, headB):
    arr = []
    currentA = headA
    while currentA != None:
        arr.append(currentA)
        currentA = currentA.next

    currentB = headB
    mergeNode = None
    while currentB != None and mergeNode == None:
        if currentB in arr:
            mergeNode = currentB
        else:
            currentB = currentB.next
    return mergeNode.data
