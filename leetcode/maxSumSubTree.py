# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        sums = {}

        def sumPostOrder(root):

            if root == None:
                return 0

            leftChild = sumPostOrder(root.left)
            rightChild = sumPostOrder(root.right)
            sumOfSubTree = root.val + leftChild + rightChild

            if sumOfSubTree not in sums:
                sums[sumOfSubTree] = 1
            else:
                sums[sumOfSubTree] += 1

            return sumOfSubTree

        sumPostOrder(root)
        maxSum = max(sums.values())

        return [v for v in sums if sums[v] == maxSum]

