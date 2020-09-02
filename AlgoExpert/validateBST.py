# https://www.algoexpert.io/questions/Validate%20BST
# time O(n) | space O(d)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validatebsthelper(tree, float("-inf"), float("inf"))


def validatebsthelper(tree, minval, maxval):
    if tree is None:
        return True

    if tree.value < minval and tree.value >= maxval:
        return False

    # leftvalid = validatebsthelper(tree.left, minval, tree.value)
    return validatebsthelper(tree.left, minval, tree.value) and validatebsthelper(tree.right, tree.value, maxval)
