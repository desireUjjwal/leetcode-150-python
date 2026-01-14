# 82. Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        curr = head
        while curr:
            if curr.val in d:
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next
        dummy = ListNode(0)
        curr = dummy
        for key, value in d.items():
            if value == 1:
                curr.next = ListNode(key)
                curr = curr.next
        return dummy.next
