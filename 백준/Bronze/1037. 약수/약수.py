import sys
input = sys.stdin.readline
n = int(input())
nums = sorted(list(map(int, input().split())))
if len(nums) % 2 == 0:
    print(nums[0] * nums[-1])
else:
    print(nums[len(nums) // 2] ** 2)