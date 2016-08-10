# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        self.result = False
        if root:
            self.walkdown(0, root)
        return self.result
        
    def walkdown(self, x, root):
        if root.left:
            self.walkdown(x+root.val, root.left)
        if root.right:
            self.walkdown(x+root.val, root.right)
        if not root.left and not root.right:
            if x+root.val == self.sum:
                self.result = True
                return
            