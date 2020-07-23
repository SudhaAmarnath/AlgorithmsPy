class BinaryTree:

    def __init__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(root):
    if root is None:
        return None
    r = invertBinaryTree(root.right)
    l = invertBinaryTree(root.left)
    root.right = l
    root.left = r

    return root