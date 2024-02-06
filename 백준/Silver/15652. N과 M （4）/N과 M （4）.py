import sys
input = sys.stdin.readline

def backtracking(temp, cnt):
	if cnt == m:
		print(*temp)
		return
	for i in range(1, n+1):
		if cnt == 0 or temp[-1] <= i:
			temp.append(i)
			backtracking(temp, cnt+1)
			temp.pop()

n, m = map(int, input().split())
temp = []
cnt = 0
backtracking(temp, cnt)