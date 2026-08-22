# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prev = dummyNode
        curr = head

        while curr:
            if curr.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
            curr = curr.next
        return dummyNode.next