import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
l = [nums[0]]
for n in nums:
	if l[-1] < n:
		l.append(n)
	else:
		idx = bisect_left(l, n)
		l[idx] = n
print(len(l))