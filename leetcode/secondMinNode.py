# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        stack = [root]
        results = []

        first = root.val
        second = 9223372036854775807

        while stack:
            current = stack.pop()

            first = min(first, current.val)

            if first < current.val < second:
                second = current.val

            if current.right:
                stack.append(current.left)
            if current.left:
                stack.append(current.right)
            results.append(current.val)

        if second == 9223372036854775807:
            return -1

        return second
        