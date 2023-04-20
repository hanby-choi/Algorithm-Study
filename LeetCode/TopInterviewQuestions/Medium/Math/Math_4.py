# pow(x, n)
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # if n % 2:
                pow *= x
            x *= x
            n >>= 1 # n = n // 2
        return pow
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # if n % 2:
                pow *= x
            x *= x
            n >>= 1 # n = n // 2
        return pow