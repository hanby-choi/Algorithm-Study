# Longest Increasing Subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        d = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and d[i] < d[j] + 1:
                    d[i] = d[j] + 1
        return max(d)
    def lengthOfLIS2(self, nums):
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                idx = bisect_left(sub, nums[i])
                sub[idx] = nums[i]
        return len(sub)