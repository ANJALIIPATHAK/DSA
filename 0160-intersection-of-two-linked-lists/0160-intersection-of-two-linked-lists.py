# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeSet = set()

        currA = headA
        while currA:
            nodeSet.add(currA)
            currA = currA.next

        currB = headB
        while currB:
            if currB in nodeSet:
                return currB
            nodeSet.add(currB)
            currB = currB.next
        return None