# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    def checkSymmetry(self, branch1, branch2):
        if branch1 == None and branch2 == None:
            return True
        elif (branch1 == None and branch2 != None) or (branch2 == None and branch1 != None):
            return False
        elif branch1.val != branch2.val:
            return False
        else:
            return self.checkSymmetry(branch1.left, branch2.right) and self.checkSymmetry(branch1.right, branch2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSymmetry(root,root)