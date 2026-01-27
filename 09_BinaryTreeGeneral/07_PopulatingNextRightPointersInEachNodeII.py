# 117. Populating Next Right Pointers in Each Node II

# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.


# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])
        while q:
            stack = []
            for i in range(len(q)):
                node = q.popleft()
                stack.append(node)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(stack)-1):
                stack[i].next = stack[i+1]

            stack = []

        return root

                
            
