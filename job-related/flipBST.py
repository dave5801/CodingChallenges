# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Flip Equivalent Binary Trees
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        else:
            if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root1.right):
                return True
            elif self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
                return True
            else:
                return False