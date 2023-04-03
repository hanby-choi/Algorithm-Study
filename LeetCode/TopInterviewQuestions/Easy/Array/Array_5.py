# Single Number
class Solution(object):
    def singleNumber(self, nums):
        compare = set()
        for num in nums:
            if num in compare:
                compare.remove(num)
            else:
                compare.add(num)
        return compare.pop()
    def singleNumber2(self, nums):
        return 2*sum(set(nums)) - sum(nums)
    def singleNumber3(self, nums):
        answer = 0
        for num in nums:
            answer = answer ^ num
        return answer