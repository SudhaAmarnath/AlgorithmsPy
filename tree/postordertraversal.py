'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        post=[]
        self.helper(root,post)
        return post
    def helper(self,root,post):
        if root is None:
            return
        self.helper(root.left,post)
        self.helper(root.right,post)
        post.append(root.val)


#solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = list()
        if not root:
            return res

        stack = list()
        stack.append(root)
        while stack:
            curr = stack[-1]
            if not curr.left and not curr.right:
                stack.pop()
                res.append(curr.val)
            else:
                if curr.right:
                    stack.append(curr.right)
                    curr.right = None
                if curr.left:
                    stack.append(curr.left)
                    curr.left = None
        return res
