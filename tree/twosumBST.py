#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        l = self.inorder(root)
        # print(l)
        s = 0
        e = len(l) - 1
        while (s < e):
            if (l[s] + l[e]) > k:
                e -= 1
            elif (l[s] + l[e]) < k:
                s += 1
            else:
                return True
        return False

    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return []
        leftlist = self.inorder(root.left)
        rightlist = self.inorder(root.right)
        return leftlist + [root.val] + rightlist