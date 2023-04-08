# Convert Sorted Array to Binary Search Tree
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.BST(0, len(nums), nums)
    def BST(self, start, end, nums):
        if start >= end:
            return None
        mid = (start+end)//2
        return TreeNode(
            val = nums[mid],
            left = self.BST(start, mid, nums),
            right = self.BST(mid+1, end, nums)
        )
    def sortedArrayToBST2(self, nums):
        def dfs(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            return TreeNode(nums[mid], dfs(left, mid-1), dfs(mid+1, right))
        return dfs(0, len(nums) - 1)