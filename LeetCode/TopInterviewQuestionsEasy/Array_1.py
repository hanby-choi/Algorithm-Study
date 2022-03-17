# 26. Remove Duplicates from Sorted Array (Easy)
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0 # start comparing from nums[0] - initialize index i
        for j in range(1, len(nums)): # compare from nums[1] to the end of nums[]
            if nums[j] != nums[i]:
                i += 1 # increase base index i for comparison
                nums[i] = nums[j] # save sorted number at nums[i]
        return i+1 # saved numbers from 0~i so the count(k) is i+1 