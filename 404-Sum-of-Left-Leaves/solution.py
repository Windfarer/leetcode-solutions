# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.walk(root)
        return self.result
        
    def walk(self, node):
        if not node:
            return
        
        if node.left:
            if node.left.left == node.left.right == None:
                self.result += node.left.val
            else:
                self.walk(node.left)
        if node.right:
            self.walk(node.right)
        