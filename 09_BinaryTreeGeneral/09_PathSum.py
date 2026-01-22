# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values
# along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumHelper(self, root: Optional[TreeNode], currSum: int, targetSum: int) -> bool:
        if root != None and root.right == None and root.left == None:
            currSum += root.val
            if targetSum == currSum:
                return True
            return False
        if root == None:
            return False
        currSum += root.val
        left = self.hasPathSumHelper(root.left, currSum, targetSum)
        right = self.hasPathSumHelper(root.right, currSum, targetSum)
        return left or right
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.hasPathSumHelper(root, 0, targetSum)
        
