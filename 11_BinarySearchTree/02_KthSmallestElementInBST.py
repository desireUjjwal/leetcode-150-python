230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], k: int) -> None:
        if root is None:
            return
        self.helper(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
            return
        self.helper(root.right, k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans, self.cnt = 0, 0
        self.helper(root, k)
        return self.ans
