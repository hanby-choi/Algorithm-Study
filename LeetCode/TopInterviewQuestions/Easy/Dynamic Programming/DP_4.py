# House Robber
class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2]+nums[i])
        return max(nums)
    def rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now