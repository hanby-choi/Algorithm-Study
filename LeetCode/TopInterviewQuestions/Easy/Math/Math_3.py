# Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n > 1 and n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False
    def isPowerOfThree2(self, n):
        if n <= 0:
            return False
        power_of_three = set()
        p = 1
        while p < 2**31:
            power_of_three.add(p)
            p *= 3
        return n in power_of_three
    def isPowerOfThree3(self, n):
        return n > 0 and 3**19 % n == 0