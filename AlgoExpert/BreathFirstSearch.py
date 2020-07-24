# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
# time O(V+E) | space O(V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]  # temp list
        while len(queue) > 0:
            current = queue.pop(
                0)  # first in first out, add childrens of each node to the end of the queue after popping to curr
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
