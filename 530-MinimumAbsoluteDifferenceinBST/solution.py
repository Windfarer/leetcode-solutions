# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mad = float("inf")
        self.walk(root)
        return self.mad
        
    def walk(self, node):
        if not node.left and not node.right:
            return node
        if node.left:
            self.walk(node.left)
            left = self.find_max(node.left)
            diff = abs(left.val - node.val)
            if diff < self.mad:
                self.mad = diff
        if node.right:
            self.walk(node.right)
            right = self.find_min(node.right)
            diff = abs(right.val - node.val)
            if diff < self.mad:
                self.mad = diff

    def find_max(self, node):
        if node.right:
            return self.find_max(node.right)
        return node
        
    def find_min(self, node):
        if node.left:
            return self.find_min(node.left)
        return node
    
