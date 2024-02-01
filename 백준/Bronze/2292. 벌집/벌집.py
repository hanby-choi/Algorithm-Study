import sys
input = sys.stdin.readline
n = int(input())
max_bound = cnt = 1
while max_bound < n:
	max_bound += cnt * 6 
	cnt += 1
print(cnt)