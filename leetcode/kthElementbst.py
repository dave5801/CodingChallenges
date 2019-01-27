# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inOrder(root, kList):
            if root:
                inOrder(root.left, kList)
                kList.append(root.val)
                inOrder(root.right, kList)
            
            return kList
    
        kthList = inOrder(root,[])
            
        return kthList[k-1]