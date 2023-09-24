import sys
input = sys.stdin.readline

def backtracking(cnt):
	if cnt == m:
		print(*temp)
		return 
	for i in range(1, n+1):
		temp.append(i)
		backtracking(cnt + 1)
		temp.pop()

n, m = map(int, input().split())
temp = []
backtracking(0)