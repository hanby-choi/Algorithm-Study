# sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        start = 0; end = x; ans = 0
        while start <= end:
            mid = (start + end) // 2
            if (mid*mid) > x:
                end = mid - 1
            elif (mid*mid) < x:
                start = mid + 1
                ans = mid
            else:
                return mid
        return ans
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
    def mySqrt(self, x):    
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r