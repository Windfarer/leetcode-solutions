# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        self.walk(root, [])
        x = None
        for a, b in zip(self.p_path, self.q_path):
            if a is b:
                x = a
                continue
        return x

    def walk(self, node, path):
        path = path+[node]
        if not node:
            return
        if node.left:
            self.walk(node.left, path)
        if node.right:
            self.walk(node.right, path)
        if node is self.p:
            self.p_path = path
            return
        elif node is self.q:
            self.q_path = path
            return
        