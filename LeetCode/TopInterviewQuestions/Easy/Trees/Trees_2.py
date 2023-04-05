# Validate Binary Search Tree
class Solution(object):
    def isValidBST(self, root):
        crnt = root
        prev = None
        stack = []
        while stack or crnt:
            if crnt:
                stack.append(crnt)
                crnt = crnt.left
            else:
                crnt = stack.pop()
                if prev != None and prev.val >= crnt.val:
                    return False
                prev = crnt
                crnt = crnt.right
        return True