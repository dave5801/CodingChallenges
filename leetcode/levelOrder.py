# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: Tree Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        result = []
        count = 1

        while q:
            currentLevel = []
            nextLevel = []

            for node in q:
                currentLevel.append(node.val)

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if count%2 == 0:
                result.append(currentLevel[::-1])
            else:
                result.append(currentLevel)
            count += 1
            q = nextLevel

        return result
        