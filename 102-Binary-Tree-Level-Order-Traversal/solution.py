# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.walk(root)
        return self.result
        
    def walk(self, node, height=0):
        if node:
            d = height + 1 - len(self.result)
            if d > 0:
                self.result.extend([[] for i in range(d)])
            self.result[height].append(node.val)
            if node.left:
                self.walk(node.left, height+1)
            if node.right:
                self.walk(node.right, height+1)

            