"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        #Adding Deep Cpies of all the nodes to the corresponding original nodes in the map
        curr = head
        while(curr):
            copy = ListNode(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        #Linking the copy nodes
        curr = head
        while(curr):
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]