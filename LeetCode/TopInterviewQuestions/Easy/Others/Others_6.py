# Missing Number
class Solution(object):
    def missingNumber(self, nums):
        check = [False] * (len(nums)+1)
        for num in nums: # O(n)
            check[num] = True
        return check.index(False) # O(n)
    def missingNumber2(self, nums):
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
    def missingNumber3(self, nums):
        nums.sort()
        if nums[0] != 0:
            return 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != (prev+1):
                return prev+1
            prev = nums[i]
        return prev+1
    def missingNumber4(self, nums):
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
    def missingNumber5(self, nums):
        return (set(range(len(nums)+1)) - set(nums)).pop()
    def missingNumber6(self, nums):
        result = 0
        for counter,value in enumerate(nums):
            result ^= counter+1 # XOR result with numbers from the complete series
            result ^= value # XOR with the numbers given in num series
        return result