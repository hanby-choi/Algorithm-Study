# 3. Symmetric Tree 
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            queue = deque([root.left, root.right])
            while queue:
                left, right = queue.popleft(), queue.popleft()
                if not left and not right:
                    continue
                if not left or not right:
                    return False
                if left.val == right.val:
                    queue += [left.left, right.right, left.right, right.left]
                else:
                    return False
            return True