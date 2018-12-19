# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [[root]]
        result = []
        count = 1

        while q:
            currentLevel = []
            nextLevel = []

            for node in q:
                current.append(node.val)

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if count%2 == 0:
                result.append(current[::-1])
            else:
                result.append(current)
            count += 1
            q = nextLevel

        return results