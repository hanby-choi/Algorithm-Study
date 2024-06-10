import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
comb = combinations(arr, 3)
max_num = 0
for c in comb:
	total = sum(c)
	if total <= m and total > max_num:
		max_num = total
print(max_num)