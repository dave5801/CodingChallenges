# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack = [root]

        prev = TreeNode(0)

        while stack:
            top = stack.pop()
            prev.right = top

            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
            top.left = None
            prev = top
