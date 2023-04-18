# Happy Number
class Solution(object):
    def isHappy(self, n):
        prev = set()
        while True:
            num = str(n)
            total = 0
            for i in num:
                total += int(i) ** 2
            if total in prev:
                return False
            elif total == 1:
                return True
            prev.add(total)
            n = total
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1
    def isHappy(self, n):
        seen = set()
        while n != 1:
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            if _sum in seen:
                return False
            seen.add(_sum)
            n = _sum
        return True