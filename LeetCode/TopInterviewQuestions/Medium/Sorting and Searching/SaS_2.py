# Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums).most_common(k)
        ans = [c[0] for c in cnt] # 튜플의 첫번째 원소: key
        return ans
    def topKFrequent2(self, nums, k):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        return sorted(list(d.keys()), key = d.get, reverse = True)[:k]
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
            
        bucketIdx = n
        ans = []
        while k > 0:
            while not bucket[bucketIdx]:  # Skip empty bucket
                bucketIdx -= 1
                
            for num in bucket[bucketIdx]:
                if k == 0: break
                ans.append(num)
                k -= 1
            bucketIdx -= 1
        return ans
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap)
            ans.append(num)
        return ans