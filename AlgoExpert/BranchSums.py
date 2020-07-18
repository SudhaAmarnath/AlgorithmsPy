# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    calculateBranchSums(root, 0, sums)  # current running sum = 0, current sums till leaf node = []
    return sums

#time O(n) | space O(n) # result list is half of length of the leaf nodes of the binary tree

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newrunningSum = runningSum + node.value  # adding sums at each level of the tree till leaf node
    if node.left is None and node.right is None:
        sums.append(newrunningSum)
        return

    calculateBranchSums(node.left, newrunningSum, sums)
    calculateBranchSums(node.right, newrunningSum, sums)  # recursive calls till leaf node is reached
