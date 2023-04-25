# 3 Sum
class Solution(object):
    def threeSum(self, nums):
        ans = set()
        nums.sort()
        for i, num in enumerate(nums):
            num_dict = {}
            for j, crnt in enumerate(nums[i+1:]):
                target = -num
                remain = target - crnt
                if remain in num_dict:
                    ans.add((num, remain, crnt))
                else:
                    num_dict[crnt] = j
        return map(list, ans)
    def threeSum2(self, nums):
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)