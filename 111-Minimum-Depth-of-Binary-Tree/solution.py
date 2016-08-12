# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.walk(root, 0)
        return self.depth
        
    def walk(self, node, depth):
        if not node:
            return
        if node and node.left is None and node.right is None:
            if self.depth == 0 or depth + 1 < self.depth:
                self.depth = depth + 1
            return
        if node.left:
            self.walk(node.left, depth + 1)
        if node.right:
            self.walk(node.right, depth + 1)