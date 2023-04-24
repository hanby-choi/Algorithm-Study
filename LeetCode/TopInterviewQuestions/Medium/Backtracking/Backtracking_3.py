# Permutation
class Solution(object):
    def permute(self, nums):
        ans = []
        n = len(nums)
        temp = [0] * n # temp = []
        visited = [False] * n
        def backtracking(cnt):
            if cnt == n:
                ans.append(temp[:])
                return
            for i in range(n):
                if not visited[i]:
                    temp[cnt] = nums[i] # temp.append(nums[i])
                    visited[i] = True
                    backtracking(cnt+1)
                    visited[i] = False
					# temp.pop()
        backtracking(0)
        return ans