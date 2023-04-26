# Find Peak Element
class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        idx = 0
        while nums[idx] < nums[idx+1]:
            idx += 1
        return idx
    def findPeakElement(self, nums):
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == (n-1) or nums[mid] > nums[mid+1]):
                return mid
            if (mid == 0 or nums[mid-1] < nums[mid]):
                low = mid + 1
            else:
                high = mid - 1
        return -1
    def findPeakElement(self, nums):
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid+1
        return i