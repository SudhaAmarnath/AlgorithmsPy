'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def f(r):
    if r==None:return
    r.left,r.right=r.right,r.left
    f(r.left)
    f(r.right)
class Solution:
    def invertTree(self, r: TreeNode) -> TreeNode:
        f(r)
        return r

#or
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        root.right = l
        root.left = r

        return root
