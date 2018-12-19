# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        results = []

        if not root:
            return results

        def dfs(root, path, results):
            if root.left:
                dfs(root.left, path+str(root.val) + '->',results)
            if root.right:
                dfs(root.right, path + str(root.val) + '->', results)
            if not root.left and not root.right:
                results.append(path + str(root.val))

        dfs(root, '', results)

        return results