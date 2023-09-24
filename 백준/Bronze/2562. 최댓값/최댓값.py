import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(9)]
max_num = max(nums)
print(max_num, nums.index(max_num) + 1)