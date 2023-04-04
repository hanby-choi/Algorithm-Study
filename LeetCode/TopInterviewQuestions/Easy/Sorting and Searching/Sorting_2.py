# First Bad Version
def isBadVersion(version):
    return
class Solution(object):
    def firstBadVersion(self, n):
        start = 1; end = n; ans = 0
        while start <= end:
            mid = int((start + end)/2)
            if isBadVersion(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans