# Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        l_depth = self.maxDepth(root.left) if root.left else 0
        r_depth = self.maxDepth(root.right) if root.right else 0
        return l_depth+1 if l_depth > r_depth else r_depth + 1