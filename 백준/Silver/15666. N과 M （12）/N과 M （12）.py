import sys
input = sys.stdin.readline

def backtracking(temp, cnt):
	if cnt == m:
		print(*temp)
		return
	for n in nums:
		if cnt == 0 or temp[-1] <= n:
			temp.append(n)
			backtracking(temp, cnt+1)
			temp.pop()

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
temp = []
cnt = 0
backtracking(temp, cnt)