#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def insert_into_bst(node, val):
            if val < node.val:
                if node.left:
                    insert_into_bst(node.left, val)
                else:
                    node.left = TreeNode(val=val)
                    return
            elif val > node.val:
                if node.right:
                    insert_into_bst(node.right, val)
                else:
                    node.right = TreeNode(val=val)
                    return

        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            insert_into_bst(root, i)
        return root