# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
516 314 4773

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        q = [root]
        count = 0

        while q:
            count += 1
            currentLevel = []
            someSeriouslyNextLevelSh__ = []

            for node in q:
                currentLevel.append(node.val)

                if node.left == None and node.right == None:
                    return count

                if node.left:
                    someSeriouslyNextLevelSh__.append(node.left)
                if node.right:
                    someSeriouslyNextLevelSh__.append(node.right)

                q = someSeriouslyNextLevelSh__
                

        return count
