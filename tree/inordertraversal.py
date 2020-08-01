'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []

        while True:

            if root:
                stack.append(root)
                root = root.left

            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right

            else:
                break

        return res