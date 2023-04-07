# Move Zeros
class Solution(object):
    def moveZeroes(self, nums):
        result = []
        zero_cnt = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_cnt += 1
        result += [0] * zero_cnt
        nums[:] = result
        return
    def moveZeroes2(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1