'''
#https://leetcode.com/problems/delete-node-in-a-bst/
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.deletekey(root, key)

    def deletekey(self, root, key):
        if root is None: return

        if root.val == key:

            if root.right and root.left:

                right = root.right  # finding inorder successor of current node
                while right.left:
                    right = right.left
                right.left = root.left  # assigning left child of root to inorder successor

                return root.right

            elif root.left:
                return root.left

            elif root.right:
                return root.right

            else:
                return None

        elif key < root.val:
            root.left = self.deletekey(root.left, key)
        else:
            root.right = self.deletekey(root.right, key)

        return root

