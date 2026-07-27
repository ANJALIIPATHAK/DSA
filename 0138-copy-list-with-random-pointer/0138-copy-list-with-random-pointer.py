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

        # Creating Deep copies of nodes and mapping them to corresponding original nodes
        curr = head
        while(curr):
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        # Linking copies with next and random pointers
        curr = head
        while(curr):
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]