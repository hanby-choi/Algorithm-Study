# Reverse Integer
class Solution(object):
    def reverse(self, x):
        maximum = 2**31
        if x >= 0:
            ans = int(str(x)[::-1])
            if 0 <= ans < maximum:
                return ans
            else:
                return 0
        else:
            ans = int(str(-x)[::-1])
            if 0 <= ans < maximum:
                return -ans
            else:
                return 0