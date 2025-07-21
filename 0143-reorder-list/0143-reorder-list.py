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
        #Finding Middle of List
        slow = head
        fast = head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        second = slow.next  # This is the beginning of the second half
        slow.next = None    #Breaking the link between first half and second half lists

        #Reversing second half:
        prev = None
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev   #This is the new head of the reversed second half list

        #Merging first and second half
        first = head

        while(second):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2





