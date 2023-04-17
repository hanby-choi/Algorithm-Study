# Sort Colors
from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        c = dict(Counter(nums))
        ans = []
        if 0 in c:
            ans += [0] * c[0]
        if 1 in c:
            ans += [1] * c[1]
        if 2 in c:
            ans += [2] * c[2]
        nums[:] = ans
    def sortColors(self, nums):
        c = Counter(nums)
        tmp = map(lambda x: [x]*c[x], c)
        ans = []
        for i in tmp:
            ans += i
        nums[:] = ans