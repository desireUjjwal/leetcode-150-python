# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        k = k % count
        if k == 0:
            return head
        
        curr = head
        for i in range(count-k-1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        curr = newHead
        while curr.next:
            curr = curr.next
        curr.next = head
        return newHead
