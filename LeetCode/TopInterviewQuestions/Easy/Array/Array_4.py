# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        compare = set()
        for num in nums:
            if num in compare:
                return True
            compare.add(num)
        return False
    def containsDuplicate2(self, nums):
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        
    def containsDuplicate3(self, nums):
        nums.sort()
        tmp = ''
        for num in nums:
            if num == tmp:
                return True
            tmp = num
        return False