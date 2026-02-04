# 530. Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.dfs(root.left)
        if self.prev:
            self.diff = min(self.diff, abs(self.prev.val - root.val))
        self.prev = root
        self.dfs(root.right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        self.prev = None
        self.dfs(root)
        return self.diff
