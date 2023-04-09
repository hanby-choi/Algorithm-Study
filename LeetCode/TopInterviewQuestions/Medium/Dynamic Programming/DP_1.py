# Jump Game
class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return True
        elif n == 2 and nums[0] >= 1:
            return True
        d = [(i+nums[i]) for i in range(n-1)]
        d[n-2] = (n-2) + nums[n-2]
        for i in range(n-3, -1, -1):
            if nums[i] > 0:
                d[i] = max(d[i:i+nums[i]+1])
        if d[0] >= (n-1):
            return True
        else:
            return False
    def canJump(self, nums):
        last = len(nums) - 1
        for i in range(n-2, -1, -1):
            if (i+nums[i] >= last):
                last = i
        return last <= 0