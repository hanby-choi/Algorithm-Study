# Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        num_2 = num_5 = 0
        for i in range(1, n+1):
            while i % 2 == 0:
                i /= 2
                num_2 += 1
            while i % 5 == 0:
                i /= 5
                num_5 += 1
        return min(num_5, num_2)
    def trailingZeroes(self, n):
        return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)
    def trailingZeroes(self, n):
        cnt = 0
        while n:
            n /= 5
            cnt += n
        return cnt