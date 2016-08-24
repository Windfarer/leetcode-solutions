# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.result = []
        self.walk(root, [])
        return ["->".join(map(str,i)) for i in self.result]
    
    def walk(self, node, collected):
        if node is not None:
            collected = collected + [node.val]
            if node is not None and node.left is None and node.right is None:
                self.result.append(collected)
                return 
            if node.left:
                self.walk(node.left, collected)
            if node.right:
                self.walk(node.right, collected)

    