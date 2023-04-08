# Shuffle an Array
import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
    def reset(self):
        return self.nums
    def shuffle(self):
        return random.sample(self.nums, len(self.nums))
    def shuffle2(self):
        return sorted(self.nums, key=lambda x: random.random())
    def shuffle(self):
        ans = list(self.original)
        for i in range(len(ans)):
            j = random.randrange(i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans
    
    def __init__(self, nums):
        self.nums = nums
        self.random = nums[:]
    def reset(self):
        return self.nums
    def shuffle3(self):
        random.shuffle(self.random)
        return self.random