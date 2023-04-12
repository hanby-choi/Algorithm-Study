# Kth Smallest Element in a BST
class Solution(object):
    def kthSmallest(self, root, k):
        crnt = root
        stack = []
        idx = 0
        while stack or crnt:
            if crnt:
                stack.append(crnt)
                crnt = crnt.left
            else:
                crnt = stack.pop()
                idx += 1
                if idx == k:
                    return crnt.val
                crnt = crnt.right
    def kthSmallest2(self, root, k):
        def inorder(root, node):
            if not root:
                return []
            else:
                inorder(root.left, node)
                node.append(root)
                inorder(root.right, node)
                return node
        
        nodelist = inorder(root, [])
        
        return nodelist[k-1].val