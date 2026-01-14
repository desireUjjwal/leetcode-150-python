# 86. Partition List

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        ptr1 = dummy1
        ptr2 = dummy2

        curr = head
        while curr:
            if curr.val < x:
                ptr1.next = ListNode(curr.val)
                ptr1 = ptr1.next
            else:
                ptr2.next = ListNode(curr.val)
                ptr2 = ptr2.next
            curr = curr.next
        ptr1.next = dummy2.next
        return dummy1.next

