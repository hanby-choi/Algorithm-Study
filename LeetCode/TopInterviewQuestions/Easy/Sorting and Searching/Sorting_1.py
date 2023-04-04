# Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        result = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i == m:
            while j < n:
                result.append(nums2[j])
                j += 1
        elif j == n:
            while i < m:
                result.append(nums1[i])
                i += 1
        nums1[:] = result