# 4.Subsets
class Solution(object):
    def subsets(self, nums):
        ans = []
        def backtracking(start, curr):
            if len(curr) == i:
                ans.append(curr[:])
                return
            for j in range(start, len(nums)):
                curr.append(nums[j])
                backtracking(j + 1, curr)
                curr.pop()
                
        for i in range(len(nums)+1):
            backtracking(0, [])
        return ans