"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        values = []

        for child in root.children:
            tmp = self.maxDepth(root.children[child])
            values.append(tmp)

        maxLevel = 0
        for v in range(len(values)):
            if maxLevel < values[v]:
                maxLevel = values[v]

        return maxLevel+1