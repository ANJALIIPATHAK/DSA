# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding middle of the list
        slow = head
        fast = head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        second = slow.next # This is the head of the second half
        slow.next = None # Breaking the link between 2 halves

        # Reversing the second half
        prev = None
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        # Merging both halves
        first = head
        while(second):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
