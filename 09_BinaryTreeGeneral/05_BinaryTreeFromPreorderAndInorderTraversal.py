105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preIndex = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder, inorder, 0, len(preorder)-1)
    
    def buildTreeHelper(self, preorder: List[int], inorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        pos = 0
        for i in range(start, end+1):
            if(inorder[i] == root.val):
                pos = i
                break
        root.left = self.buildTreeHelper(preorder, inorder, start, pos-1)
        root.right = self.buildTreeHelper(preorder, inorder, pos+1, end)
        return root
