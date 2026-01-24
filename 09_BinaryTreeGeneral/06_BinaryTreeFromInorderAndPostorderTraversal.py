# 106. Construct Binary Tree from Inorder and Postorder Traversal

# ven two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree,
# construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    postIndex = 0
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postIndex = len(postorder) - 1
        return self.buildTreeHelper(inorder, postorder, 0, len(postorder)-1)
    
    def buildTreeHelper(self, inorder: List[int], postorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        root = TreeNode(postorder[self.postIndex])
        self.postIndex -= 1
        pos = 0
        for i in range(start, end+1):
            if root.val == inorder[i]:
                pos = i
                break
        
        root.right = self.buildTreeHelper(inorder, postorder, pos+1, end)
        root.left = self.buildTreeHelper(inorder, postorder, start, pos-1) 
        return root
