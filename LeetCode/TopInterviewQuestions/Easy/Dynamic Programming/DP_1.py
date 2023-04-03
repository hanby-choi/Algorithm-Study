# Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        d = [0 for i in range(n+1)]
        d[1] = 1; d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]
    def climbStairs2(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        two_before = 1; one_before = 2; ans = 0
        for i in range(3, n+1):
            ans = one_before + two_before
            two_before = one_before
            one_before = ans
        return ans
        