# O(n) time | O(log(n)) space
class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None


def maxPathSum(tree):
    # Write your code here.
    maxPath, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    lsb, ls = findMaxSum(tree.left)
    rsb, rs = findMaxSum(tree.right)
    mcsb = max(lsb, rsb)

    value = tree.value
    msb = max(mcsb + value, value)
    msv = max(msb, lsb + value + rsb)
    mps = max(ls, rs, msv)

    return msb, mps