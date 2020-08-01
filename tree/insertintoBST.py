#https://leetcode.com/problems/insert-into-a-binary-search-tree/

'''
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(node, val):
		    # Checking for direction for tree traversal
            if node.val > val:
                if node.left:
					# Has left node, traverse it
                    dfs(node.left, val)
                else:
					# No left node, insert value
                    node.left = TreeNode(val)
            else:
                if node.right:
					# Has right node, traverse it
                    dfs(node.right, val)
                else:
					# No right node, insert val
                    node.right = TreeNode(val)
        if root:
			# Root is valid
            dfs(root, val)
            return root
        else:
			# Empty root, insert value
            return TreeNode(val)