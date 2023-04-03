# Rotate Array
nums = list(map(int, input().split()))
k = int(input())
def a(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]