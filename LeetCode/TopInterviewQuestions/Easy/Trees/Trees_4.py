# Binary Tree Level Order Traversal
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        queue = deque([root])
        result = []
        while queue:
            child, parent_val = deque(), []
            while queue:
                parent = queue.popleft()
                parent_val.append(parent.val)
                if parent.left:
                    child.append(parent.left)
                if parent.right:
                    child.append(parent.right)
            queue = child
            result.append(parent_val)  
        return result
    def levelOrder2(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [leaf for leaf in tmp if leaf] # removing None nodes in tmp
        return ans