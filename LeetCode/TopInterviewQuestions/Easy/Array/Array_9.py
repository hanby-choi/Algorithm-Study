# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        complement = {}
        for i, num in enumerate(nums):
            remaining = target-num
            if remaining in complement:
                return (i, complement[remaining])
            complement[num] = i