"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        result = []

        while q:
            currentLevel = []
            nextLevel = []

            for node in q:
                currentLevel.append(node.val)
                for child in node.children:
                    nextLevel.append(child)

            result.append(currentLevel)
            q = nextLevel

        return result