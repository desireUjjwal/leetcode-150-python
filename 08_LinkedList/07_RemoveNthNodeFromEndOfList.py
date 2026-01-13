# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        count_from_beg = count - n
        if count_from_beg == 0:
            return head.next
        i = 0
        curr = head
        while i < count_from_beg-1:
            i += 1
            curr = curr.next

        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head
