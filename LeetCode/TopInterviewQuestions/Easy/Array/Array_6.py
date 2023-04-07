# intersection of Two Arrays 2
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        intersection = {}
        result = []
        c1 = Counter(nums1) # {1:1, 2:1, ...}
        c2 = Counter(nums2)
        if len(c1) <= len(c2):
            for key, value in c1.items():
                if key in c2:
                    intersection[key] = min(c1[key], c2[key])
        else:
            for key, value in c2.items():
                if key in c1:
                    intersection[key] = min(c1[key], c2[key])
        for key, value in intersection.items():
            result += [key] * value
        return result
    def intersect2(self, nums1, nums2):
        if len(nums1) > len(nums2): return self.intersect2(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans