import sys
input = sys.stdin.readline
n = int(input())
max_bound = cnt = 1
while max_bound < n:
	cnt += 1
	max_bound += cnt * 6 - 6
print(cnt)