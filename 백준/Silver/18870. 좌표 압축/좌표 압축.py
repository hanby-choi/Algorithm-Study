import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
unique_nums = sorted(list(set(nums)))
index = [i for i in range(len(unique_nums))]
num_dict = {k: v for k, v in zip(unique_nums, index)}
for n in nums:
	print(num_dict[n], end=' ')