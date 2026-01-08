# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            elif list1:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        return dummy.next
