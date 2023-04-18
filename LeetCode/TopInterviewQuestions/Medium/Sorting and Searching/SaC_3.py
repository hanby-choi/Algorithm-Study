# Kth Largest Element in an Array
class Solution(object):
    def findKthLargest(self, nums, k):
        nums[:] = list(map(lambda x: x*-1, nums))
        heapq.heapify(nums)
        for i in range(k):
            ans = -heapq.heappop(nums)
        return ans
    def fKLHeap(nums, k):
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L+M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]