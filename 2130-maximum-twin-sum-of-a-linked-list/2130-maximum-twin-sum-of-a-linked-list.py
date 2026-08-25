# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = ListNode(0, head)
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev

        l1 = head

        maxSum = float("-inf")

        while l1 and l2:
            sum = l1.val + l2.val
            maxSum = max(maxSum, sum)
            l1 = l1.next
            l2 = l2.next

        return maxSum