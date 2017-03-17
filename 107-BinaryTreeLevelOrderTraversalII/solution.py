# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.walk(0, root)
        return list(reversed(self.result))
    def walk(self, h, node):
        if not node:
            return
        if len(self.result) - 1 < h:
            self.result.append([])
        self.result[h].append(node.val)
        self.walk(h+1, node.left)
        self.walk(h+1, node.right)
