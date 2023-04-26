# Search for a Range (Find First and Last Position of Element in Sorted Array)
class Solution(object):
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        l, r = 0, len(nums)-1
        start, end = -1, -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                start = end = mid
                break
        while (start-1) >= 0 and nums[start-1] == target:
            start -= 1
        while (end+1) < len(nums) and nums[end+1] == target:
            end += 1
        return [start, end]
    def searchRange(self, nums, target):
        import bisect
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)-1
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
    def searchRange(self, nums, target):
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]